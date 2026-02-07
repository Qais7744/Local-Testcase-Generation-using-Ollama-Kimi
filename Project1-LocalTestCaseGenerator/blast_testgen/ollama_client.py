"""Ollama API client for local LLM communication."""

import requests
import time
from typing import Optional, Dict, Any


class OllamaClient:
    """Client for interacting with Ollama local LLM server."""
    
    DEFAULT_HOST = "http://localhost:11434"
    DEFAULT_MODEL = "llama3.2"
    MAX_RETRIES = 3
    RETRY_DELAY = 2
    
    def __init__(self, host: str = None, model: str = None):
        self.host = host or self.DEFAULT_HOST
        self.model = model or self.DEFAULT_MODEL
        self.api_url = f"{self.host}/api/generate"
    
    def is_available(self) -> bool:
        """Check if Ollama server is running."""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def generate(
        self, 
        prompt: str, 
        temperature: float = 0.2,
        num_predict: int = 2048,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Generate text using Ollama API.
        
        Args:
            prompt: The prompt text
            temperature: Creativity level (0.0 to 1.0)
            num_predict: Max tokens to generate
            stream: Whether to stream response
            
        Returns:
            Dict containing 'response' and 'done' status
            
        Raises:
            ConnectionError: If Ollama is not available
            RuntimeError: If generation fails after retries
        """
        if not self.is_available():
            raise ConnectionError(
                f"Ollama not available at {self.host}. "
                "Make sure Ollama is running (ollama serve)"
            )
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "options": {
                "temperature": temperature,
                "num_predict": num_predict
            }
        }
        
        last_error = None
        for attempt in range(self.MAX_RETRIES):
            try:
                response = requests.post(
                    self.api_url,
                    json=payload,
                    timeout=300
                )
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                last_error = e
                if attempt < self.MAX_RETRIES - 1:
                    time.sleep(self.RETRY_DELAY * (attempt + 1))
        
        raise RuntimeError(
            f"Failed to generate after {self.MAX_RETRIES} attempts: {last_error}"
        )
    
    def list_models(self) -> list:
        """List available models in Ollama."""
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            response.raise_for_status()
            data = response.json()
            return [m["name"] for m in data.get("models", [])]
        except requests.RequestException as e:
            raise ConnectionError(f"Cannot list models: {e}")
