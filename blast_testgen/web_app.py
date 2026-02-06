"""Web application for Testcase Generator Chat UI."""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import sys
import json
import re

from .ollama_client import OllamaClient
from .prompts import build_test_prompt

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# Initialize Ollama client
client = OllamaClient()


@app.route('/')
def index():
    """Render the chat UI."""
    return render_template('chat.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if Ollama is available."""
    is_available = client.is_available()
    models = []
    if is_available:
        try:
            models = client.list_models()
        except:
            pass
    return jsonify({
        'status': 'healthy' if is_available else 'ollama_unavailable',
        'ollama_connected': is_available,
        'model': client.model,
        'available_models': models
    })


@app.route('/api/generate', methods=['POST'])
def generate_tests():
    """Generate testcases from user input."""
    data = request.get_json()
    
    if not data or 'code' not in data:
        return jsonify({'error': 'No input provided'}), 400
    
    user_input = data['code'].strip()
    
    if len(user_input) < 2:
        return jsonify({
            'error': 'Input too short',
            'hint': 'Please provide at least 2 characters'
        }), 400
    
    # Check Ollama availability
    if not client.is_available():
        return jsonify({
            'error': 'Ollama not available. Please start Ollama server.',
            'hint': 'Run: ollama serve'
        }), 503
    
    try:
        # Check if it's a URL/website
        if is_url(user_input):
            return generate_website_tests(user_input)
        
        # Check if it looks like Python code
        is_code = looks_like_code(user_input)
        
        # For non-code inputs, ALWAYS use quick generation (no LLM)
        if not is_code:
            return generate_feature_tests(user_input)
        
        # For code inputs, use LLM with timeout handling
        return generate_code_tests(user_input)
        
    except Exception as e:
        # Fallback to quick generation on any error
        return generate_feature_tests(user_input, fallback=True)


def is_url(text: str) -> bool:
    """Check if input is a URL or domain."""
    clean_text = text.lower().strip()
    
    # Common TLDs
    tlds = ['.com', '.org', '.net', '.io', '.app', '.co', '.in', '.dev', '.ai']
    
    # Check if it ends with a TLD
    for tld in tlds:
        if clean_text.endswith(tld):
            return True
    
    # Check for domain pattern
    if re.match(r'^[\w\-]+\.[\w\-]+', clean_text):
        return True
    
    # Check for http/https
    if clean_text.startswith('http'):
        return True
    
    return False


def looks_like_code(text: str) -> bool:
    """Check if input looks like Python code."""
    code_indicators = [
        'def ',
        'class ',
        'import ',
        'return ',
        'if ',
        'for ',
        'while ',
        'try:',
        'except',
        'self.',
        '():',
        'print(',
        '# '
    ]
    
    for indicator in code_indicators:
        if indicator in text:
            return True
    
    return False


def generate_website_tests(url: str) -> dict:
    """Generate test cases for website testing."""
    domain = url.replace('https://', '').replace('http://', '').strip('/')
    
    test_cases = [
        {
            "id": "TC_001",
            "title": f"Page load - {domain}",
            "type": "POSITIVE",
            "steps": [
                f"Navigate to {url}",
                "Wait for page to fully load",
                "Verify page title is displayed"
            ],
            "expected": f"Page should load successfully with correct title"
        },
        {
            "id": "TC_002",
            "title": "Verify all images load correctly",
            "type": "POSITIVE",
            "steps": [
                f"Open {url}",
                "Scroll through entire page",
                "Check all images are visible"
            ],
            "expected": "All images should load without 404 errors"
        },
        {
            "id": "TC_003",
            "title": "Responsive design - Mobile view",
            "type": "POSITIVE",
            "steps": [
                f"Open {url} in mobile viewport",
                "Verify all elements are visible",
                "Check for horizontal scroll"
            ],
            "expected": "Page should be responsive, no horizontal scrollbar"
        },
        {
            "id": "TC_004",
            "title": "Form validation - Empty submission",
            "type": "NEGATIVE",
            "steps": [
                f"Navigate to {url}",
                "Click submit without filling fields",
                "Observe validation messages"
            ],
            "expected": "Appropriate validation error messages should be displayed"
        },
        {
            "id": "TC_005",
            "title": "Page load performance",
            "type": "POSITIVE",
            "steps": [
                f"Open browser DevTools",
                f"Navigate to {url}",
                "Check page load time"
            ],
            "expected": "Page should load within 3 seconds"
        },
        {
            "id": "TC_006",
            "title": "404 Error page handling",
            "type": "NEGATIVE",
            "steps": [
                f"Navigate to {url}/nonexistent-page",
                "Observe the error page"
            ],
            "expected": "Custom 404 error page should be displayed"
        }
    ]
    
    pytest_code = f'''import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_page_load(browser):
    """Test that {domain} loads successfully"""
    browser.get("https://{domain}")
    assert browser.title != ""
    assert "{domain.split('.')[0]}" in browser.current_url

def test_responsive_mobile(browser):
    """Test mobile responsiveness"""
    browser.set_window_size(375, 812)
    browser.get("https://{domain}")
    body = browser.find_element(By.TAG_NAME, "body")
    body_width = body.size['width']
    assert body_width <= 375
'''
    
    return jsonify({
        'success': True,
        'test_cases': test_cases,
        'pytest_code': pytest_code,
        'model_used': 'website-mode',
        'input_length': len(url),
        'note': f'Website testing: {domain}'
    })


def generate_feature_tests(user_input: str, fallback: bool = False) -> dict:
    """Generate test cases for feature/requirement text (no LLM)."""
    
    # Extract keywords from input
    words = user_input.lower().split()
    feature_name = ' '.join(words[:5]) if len(words) > 5 else user_input
    
    test_cases = [
        {
            "id": "TC_001",
            "title": f"Valid {feature_name[:40]} - Success scenario",
            "type": "POSITIVE",
            "steps": [
                "Navigate to the feature/module",
                "Provide valid input/data",
                "Execute the action"
            ],
            "expected": "Feature should work correctly with success message"
        },
        {
            "id": "TC_002",
            "title": "Empty/Blank input validation",
            "type": "NEGATIVE",
            "steps": [
                "Navigate to the feature",
                "Leave required fields empty",
                "Submit the form/action"
            ],
            "expected": "Validation error: 'This field is required' should be shown"
        },
        {
            "id": "TC_003",
            "title": "Invalid data format",
            "type": "NEGATIVE",
            "steps": [
                "Navigate to the feature",
                "Enter data in wrong format (e.g., text in number field)",
                "Submit the form"
            ],
            "expected": "Validation error for invalid format should be displayed"
        },
        {
            "id": "TC_004",
            "title": "Maximum length boundary test",
            "type": "NEGATIVE",
            "steps": [
                "Navigate to the feature",
                "Enter data exceeding maximum allowed length",
                "Submit the form"
            ],
            "expected": "Error message: 'Maximum length exceeded' should be shown"
        },
        {
            "id": "TC_005",
            "title": "Session timeout handling",
            "type": "NEGATIVE",
            "steps": [
                "Login and navigate to feature",
                "Wait for session to expire",
                "Try to use the feature"
            ],
            "expected": "User should be redirected to login page with timeout message"
        }
    ]
    
    pytest_code = f'''import pytest

def test_valid_{feature_name[:20].replace(" ", "_").replace(".", "")}():
    """Test {feature_name[:50]} with valid input"""
    # Arrange
    input_data = "valid_data"
    
    # Act
    result = process_input(input_data)
    
    # Assert
    assert result is not None
    assert result["success"] == True

def test_empty_input_validation():
    """Test validation for empty input"""
    input_data = ""
    with pytest.raises(ValueError, match="required"):
        process_input(input_data)

def test_invalid_format():
    """Test validation for invalid format"""
    input_data = "invalid_format"
    with pytest.raises(ValueError):
        process_input(input_data)

def test_max_length():
    """Test maximum length validation"""
    input_data = "x" * 1000  # Exceeds max length
    with pytest.raises(ValueError, match="length"):
        process_input(input_data)
'''
    
    return jsonify({
        'success': True,
        'test_cases': test_cases,
        'pytest_code': pytest_code,
        'model_used': 'quick-mode',
        'input_length': len(user_input),
        'note': 'Quick generation' + (' (LLM fallback)' if fallback else ' - Instant results')
    })


def generate_code_tests(user_input: str) -> dict:
    """Generate test cases for Python code using LLM."""
    try:
        prompt = build_test_prompt(user_input)
        
        response = client.generate(
            prompt=prompt,
            temperature=0.2,
            num_predict=1500
        )
        
        generated_text = response.get('response', '')
        result = parse_combined_response(generated_text)
        
        return jsonify({
            'success': True,
            'test_cases': result.get('manual_test_cases', []),
            'pytest_code': result.get('pytest_code', ''),
            'model_used': client.model,
            'input_length': len(user_input)
        })
    except Exception as e:
        # If LLM fails, fallback to quick generation
        return generate_feature_tests(user_input, fallback=True)


def parse_combined_response(text: str) -> dict:
    """Parse combined JSON response with manual test cases and pytest code."""
    result = {
        'manual_test_cases': [],
        'pytest_code': ''
    }
    
    # Try to extract JSON from markdown code blocks
    json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if json_match:
        text = json_match.group(1)
    
    # Try to find JSON object
    obj_match = re.search(r'\{[\s\S]*\}', text)
    if obj_match:
        text = obj_match.group(0)
    
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            # Extract manual test cases
            if 'manual_test_cases' in data:
                result['manual_test_cases'] = data['manual_test_cases']
            elif 'test_cases' in data:
                result['manual_test_cases'] = data['test_cases']
            
            # Extract pytest code
            if 'pytest_code' in data:
                result['pytest_code'] = data['pytest_code']
            elif 'python_code' in data:
                result['pytest_code'] = data['python_code']
            
            return result
    except json.JSONDecodeError:
        pass
    
    # Fallback: try to extract pytest code block
    code_match = re.search(r'```python\s*([\s\S]*?)\s*```', text)
    if code_match:
        result['pytest_code'] = code_match.group(1)
    else:
        result['pytest_code'] = text
    
    # Create a simple info test case
    result['manual_test_cases'] = [{
        "id": "TC_001",
        "title": "Generated Test",
        "type": "INFO",
        "steps": ["See generated pytest code below"],
        "expected": "Code should execute successfully"
    }]
    
    return result


def run_web_app(host='127.0.0.1', port=5000, debug=False):
    """Run the Flask web application."""
    print(f"Starting Testcase Generator UI")
    print(f"   URL: http://{host}:{port}")
    print(f"   Model: {client.model}")
    print(f"   Press Ctrl+C to stop")
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run_web_app(debug=True)
