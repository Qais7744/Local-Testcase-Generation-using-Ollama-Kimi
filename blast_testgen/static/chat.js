/**
 * BLAST Testcase Generator - Combined Manual + Code UI
 */

const messagesContainer = document.getElementById('messages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');
const loadingOverlay = document.getElementById('loadingOverlay');
const statusEl = document.getElementById('status');

// Example inputs
const EXAMPLES = {
    login: `def login(username, password):
    if not username or not password:
        raise ValueError("Required")
    if len(password) < 6:
        raise ValueError("Too short")
    return {"token": "abc123"}`,
    
    calculator: `def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b`,
    
    signup: `def register(email, password):
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"id": 1, "email": email}`
};

// Request timeout in milliseconds (2 minutes for code generation)
const REQUEST_TIMEOUT = 120000;

document.addEventListener('DOMContentLoaded', () => {
    checkStatus();
    initEventListeners();
});

function initEventListeners() {
    sendBtn.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            sendMessage();
        }
    });
    
    clearBtn.addEventListener('click', () => {
        userInput.value = '';
        userInput.style.height = 'auto';
        userInput.focus();
    });
    
    document.querySelectorAll('.example-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const example = btn.dataset.example;
            if (EXAMPLES[example]) {
                userInput.value = EXAMPLES[example];
                autoResize();
                userInput.focus();
            }
        });
    });
    
    userInput.addEventListener('input', autoResize);
}

function autoResize() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 300) + 'px';
}

async function checkStatus() {
    try {
        const response = await fetch('/api/health');
        const data = await response.json();
        
        if (data.ollama_connected) {
            statusEl.className = 'status connected';
            statusEl.querySelector('.status-text').textContent = 'Ready';
        } else {
            statusEl.className = 'status error';
            statusEl.querySelector('.status-text').textContent = 'Offline';
            addSystemMessage('Ollama is not running. Please start it with: ollama serve', 'error');
        }
    } catch (error) {
        statusEl.className = 'status error';
        statusEl.querySelector('.status-text').textContent = 'Error';
    }
}

async function sendMessage() {
    const userInput_text = userInput.value.trim();
    if (!userInput_text) return;
    
    if (userInput_text.length < 3) {
        addErrorMessage('Input too short', 'Please provide at least 3 characters');
        return;
    }

    addUserMessage(userInput_text);
    
    userInput.value = '';
    userInput.style.height = 'auto';
    
    showLoading();
    
    // Create abort controller for timeout
    const controller = new AbortController();
    const timeoutId = setTimeout(() => {
        controller.abort();
    }, REQUEST_TIMEOUT);

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: userInput_text }),
            signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        hideLoading();

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `HTTP ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            addErrorMessage(data.error, data.hint);
        } else {
            addCombinedResult(data.test_cases, data.pytest_code, data.note);
        }
    } catch (error) {
        hideLoading();
        clearTimeout(timeoutId);
        
        if (error.name === 'AbortError') {
            addErrorMessage('Request timed out', 'The generation took too long. Try with simpler code or check if Ollama is responding.');
        } else {
            addErrorMessage(error.message || 'Failed to connect to server', 'Make sure the server is running');
        }
    }
}

function addUserMessage(text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user-message';
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>`;
    
    const content = document.createElement('div');
    content.className = 'content';
    
    const pre = document.createElement('pre');
    const code = document.createElement('code');
    code.className = 'language-python';
    code.textContent = text;
    pre.appendChild(code);
    content.appendChild(pre);
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    messagesContainer.appendChild(messageDiv);
    
    scrollToBottom();
}

function addSystemMessage(text, type = 'info') {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerHTML = '!';
    
    const content = document.createElement('div');
    content.className = 'content';
    
    if (type === 'error') {
        content.style.background = 'rgba(239, 68, 68, 0.1)';
        content.style.border = '1px solid var(--error)';
    }
    
    content.innerHTML = `<p>${escapeHtml(text)}</p>`;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    messagesContainer.appendChild(messageDiv);
    
    scrollToBottom();
}

function addCombinedResult(testCases, pytestCode, note) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="9" x2="15" y2="9"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>`;
    
    const content = document.createElement('div');
    content.className = 'content test-cases-content';
    
    let html = `
        <div class="test-cases-header">
            <h3>Coverage Summary: ${testCases.length} test cases generated</h3>
            ${note ? `<span class="quick-mode-badge">${escapeHtml(note)}</span>` : ''}
        </div>
        <div class="test-cases-grid">
    `;
    
    // Add manual test case cards
    testCases.forEach((tc) => {
        const typeClass = tc.type === 'POSITIVE' ? 'positive' : (tc.type === 'NEGATIVE' ? 'negative' : 'neutral');
        const typeLabel = tc.type || 'TEST';
        
        const stepsHtml = tc.steps.map((step, i) => 
            `<li><span class="step-num">${i + 1}.</span> ${escapeHtml(step)}</li>`
        ).join('');
        
        html += `
            <div class="test-case-card ${typeClass}">
                <div class="test-case-header">
                    <span class="test-case-id">${escapeHtml(tc.id)}</span>
                    <span class="test-case-badge ${typeClass}">${typeLabel}</span>
                </div>
                <h4 class="test-case-title">${escapeHtml(tc.title)}</h4>
                <div class="test-case-steps">
                    <label>Steps:</label>
                    <ol>${stepsHtml}</ol>
                </div>
                <div class="test-case-expected">
                    <label>Expected:</label>
                    <p>${escapeHtml(tc.expected)}</p>
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    
    // Add pytest code section
    if (pytestCode) {
        const codeBlockId = 'pytest-' + Date.now();
        html += `
            <div class="pytest-section">
                <div class="pytest-header">
                    <h4>Automation Code (pytest)</h4>
                    <button class="copy-btn" onclick="copyCode('${codeBlockId}', this)">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                        </svg>
                        Copy Code
                    </button>
                </div>
                <div class="code-block-wrapper">
                    <pre><code id="${codeBlockId}" class="language-python">${escapeHtml(pytestCode)}</code></pre>
                </div>
            </div>
        `;
    }
    
    // Add export button
    html += `
        <div class="test-cases-actions">
            <button class="export-btn" onclick="exportAll()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Export All
            </button>
        </div>
    `;
    
    content.innerHTML = html;
    
    // Store data for export
    content.dataset.testCases = JSON.stringify(testCases);
    content.dataset.pytestCode = pytestCode;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    messagesContainer.appendChild(messageDiv);
    
    // Highlight code if hljs is available
    if (typeof hljs !== 'undefined') {
        const codeEl = content.querySelector('code');
        if (codeEl) hljs.highlightElement(codeEl);
    }
    
    scrollToBottom();
}

function addErrorMessage(error, hint) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    
    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.style.background = 'var(--error)';
    avatar.innerHTML = '!';
    
    const content = document.createElement('div');
    content.className = 'content';
    content.style.background = 'rgba(239, 68, 68, 0.1)';
    content.style.border = '1px solid var(--error)';
    
    let html = `<p style="color: var(--error); font-weight: 500;">${escapeHtml(error)}</p>`;
    if (hint) {
        html += `<p style="margin-top: 0.5rem; font-size: 0.875rem; color: var(--text-secondary);">${escapeHtml(hint)}</p>`;
    }
    
    content.innerHTML = html;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    messagesContainer.appendChild(messageDiv);
    
    scrollToBottom();
}

function showLoading() {
    loadingOverlay.classList.add('active');
    sendBtn.disabled = true;
}

function hideLoading() {
    loadingOverlay.classList.remove('active');
    sendBtn.disabled = false;
}

function scrollToBottom() {
    const chatContainer = document.querySelector('.chat-container');
    chatContainer.scrollTo({
        top: chatContainer.scrollHeight,
        behavior: 'smooth'
    });
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function copyCode(elementId, btn) {
    const codeEl = document.getElementById(elementId);
    const text = codeEl.textContent;
    
    navigator.clipboard.writeText(text).then(() => {
        btn.classList.add('copied');
        const originalHtml = btn.innerHTML;
        btn.innerHTML = `
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            Copied!
        `;
        
        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = originalHtml;
        }, 2000);
    });
}

function exportAll() {
    const testCasesContent = document.querySelector('.test-cases-content');
    if (!testCasesContent) {
        alert('No test cases to export');
        return;
    }
    
    const testCases = JSON.parse(testCasesContent.dataset.testCases || '[]');
    const pytestCode = testCasesContent.dataset.pytestCode || '';
    
    const exportData = {
        manual_test_cases: testCases,
        pytest_code: pytestCode,
        exported_at: new Date().toISOString()
    };
    
    const jsonStr = JSON.stringify(exportData, null, 2);
    
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'test_cases.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Make functions globally available
window.copyCode = copyCode;
window.exportAll = exportAll;
