# SOP-003: Ollama Integration

## Goal
Reliable communication with local Ollama server.

## Connection Parameters
- Host: `http://localhost:11434`
- Timeout: 300s (generation can be slow)
- Retries: 3 with exponential backoff

## API Schema

### Request
```json
{
  "model": "llama3.2",
  "prompt": "string",
  "stream": false,
  "options": {
    "temperature": 0.2,
    "num_predict": 2048
  }
}
```

### Response
```json
{
  "response": "generated text",
  "done": true
}
```

## Health Check
- Endpoint: GET /api/tags
- Expected: 200 OK with model list
- Retry: 3 times with 2s delay

## Failure Handling
1. Check if Ollama is running
2. Check if model is pulled
3. Retry with backoff
4. Return user-friendly error
