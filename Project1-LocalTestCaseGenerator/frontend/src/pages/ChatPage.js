import React, { useState, useRef, useEffect } from 'react';
import {
  Box,
  Paper,
  TextField,
  Button,
  Typography,
  Chip,
  IconButton,
  Divider,
  Alert,
  Snackbar,
  Fade,
  Tooltip,
  Avatar,
  Card,
  CardContent,
  Stack,
  Container,
  LinearProgress,
  Fab,
  Zoom,
} from '@mui/material';
import {
  Send as SendIcon,
  Clear as ClearIcon,
  ContentCopy as CopyIcon,
  Check as CheckIcon,
  Code as CodeIcon,
  AutoAwesome as AIIcon,
  Computer as ComputerIcon,
  Speed as SpeedIcon,
  Security as SecurityIcon,
  Download as DownloadIcon,
  Delete as DeleteIcon,
} from '@mui/icons-material';
import { checkHealth, generateTests } from '../services/api';
import TestCaseCard from '../components/TestCaseCard';
import CodeBlock from '../components/CodeBlock';

const EXAMPLES = [
  {
    id: 'login',
    label: 'Login Function',
    code: `def login(username, password):
    if not username or not password:
        raise ValueError("Required")
    return {"token": "abc123"}`,
  },
  {
    id: 'calculator',
    label: 'Calculator',
    code: `def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b`,
  },
  {
    id: 'registration',
    label: 'Registration',
    code: `def register(email, password):
    if "@" not in email:
        raise ValueError("Invalid email")
    return {"id": 1, "email": email}`,
  },
];

const ChatPage = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState({ connected: false, model: '' });
  const [error, setError] = useState(null);
  const [copied, setCopied] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  // Scroll to bottom
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Check Ollama status on load
  useEffect(() => {
    checkHealth()
      .then((data) => {
        setStatus({
          connected: data.ollama_connected,
          model: data.model,
        });
      })
      .catch(() => {
        setStatus({ connected: false, model: '' });
      });
  }, []);

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    const userMessage = input.trim();
    setInput('');
    setLoading(true);
    setError(null);

    // Add user message
    setMessages((prev) => [
      ...prev,
      {
        type: 'user',
        content: userMessage,
      },
    ]);

    try {
      const data = await generateTests(userMessage);

      // Add bot response
      setMessages((prev) => [
        ...prev,
        {
          type: 'bot',
          testCases: data.test_cases || [],
          pytestCode: data.pytest_code || '',
          note: data.note || '',
          model: data.model_used,
        },
      ]);
    } catch (err) {
      setError(err.message || 'Failed to generate test cases');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && e.ctrlKey) {
      handleSend();
    }
  };

  const loadExample = (example) => {
    setInput(example.code);
    inputRef.current?.focus();
  };

  const clearChat = () => {
    setMessages([]);
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const exportAll = () => {
    const lastMessage = messages.filter((m) => m.type === 'bot').pop();
    if (!lastMessage) return;

    const exportData = {
      manual_test_cases: lastMessage.testCases,
      pytest_code: lastMessage.pytestCode,
      exported_at: new Date().toISOString(),
    };

    const blob = new Blob([JSON.stringify(exportData, null, 2)], {
      type: 'application/json',
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'test_cases.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <Box sx={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <Paper
        elevation={0}
        sx={{
          p: 2,
          background: 'rgba(30, 41, 59, 0.8)',
          backdropFilter: 'blur(10px)',
          borderBottom: '1px solid rgba(255,255,255,0.1)',
        }}
      >
        <Container maxWidth="lg">
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
              <Avatar
                sx={{
                  bgcolor: 'primary.main',
                  background: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
                }}
              >
                <AIIcon />
              </Avatar>
              <Box>
                <Typography variant="h6" fontWeight="700">
                  Local Test Case Generator
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  AI-Powered Testing with Ollama
                </Typography>
              </Box>
            </Box>

            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
              <Chip
                size="small"
                icon={<ComputerIcon />}
                label={status.model || 'llama3.2'}
                color="primary"
                variant="outlined"
              />
              <Chip
                size="small"
                icon={<SpeedIcon />}
                label={status.connected ? 'Ready' : 'Offline'}
                color={status.connected ? 'success' : 'error'}
                sx={{
                  '& .MuiChip-icon': {
                    color: status.connected ? 'success.main' : 'error.main',
                  },
                }}
              />
              {messages.length > 0 && (
                <Tooltip title="Clear chat">
                  <IconButton onClick={clearChat} color="error" size="small">
                    <DeleteIcon />
                  </IconButton>
                </Tooltip>
              )}
            </Box>
          </Box>
        </Container>
      </Paper>

      {/* Welcome Banner */}
      {messages.length === 0 && (
        <Fade in={messages.length === 0}>
          <Container maxWidth="md" sx={{ mt: 4, mb: 2 }}>
            <Paper
              sx={{
                p: 4,
                textAlign: 'center',
                background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1))',
                border: '1px solid rgba(99, 102, 241, 0.3)',
                borderRadius: 3,
              }}
            >
              <AIIcon sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
              <Typography variant="h4" gutterBottom fontWeight="600">
                Welcome to AI Test Engineer
              </Typography>
              <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
                I generate comprehensive test cases from your Python code or feature descriptions.
                Everything runs locally using Ollama - your code never leaves your machine!
              </Typography>
              <Stack direction="row" spacing={2} justifyContent="center" sx={{ mb: 3 }}>
                <Box sx={{ textAlign: 'center' }}>
                  <SecurityIcon color="success" sx={{ fontSize: 32, mb: 1 }} />
                  <Typography variant="caption" display="block">100% Local</Typography>
                </Box>
                <Box sx={{ textAlign: 'center' }}>
                  <CodeIcon color="primary" sx={{ fontSize: 32, mb: 1 }} />
                  <Typography variant="caption" display="block">pytest Ready</Typography>
                </Box>
                <Box sx={{ textAlign: 'center' }}>
                  <SpeedIcon color="warning" sx={{ fontSize: 32, mb: 1 }} />
                  <Typography variant="caption" display="block">Fast Generation</Typography>
                </Box>
              </Stack>
            </Paper>
          </Container>
        </Fade>
      )}

      {/* Example Chips */}
      {messages.length === 0 && (
        <Container maxWidth="md" sx={{ mb: 2 }}>
          <Typography variant="caption" color="text.secondary" sx={{ mb: 1, display: 'block' }}>
            Try an example:
          </Typography>
          <Stack direction="row" spacing={1} flexWrap="wrap" useFlexGap>
            {EXAMPLES.map((example) => (
              <Chip
                key={example.id}
                label={example.label}
                onClick={() => loadExample(example)}
                clickable
                sx={{
                  '&:hover': {
                    bgcolor: 'primary.main',
                    color: 'white',
                  },
                }}
              />
            ))}
          </Stack>
        </Container>
      )}

      {/* Chat Messages */}
      <Box sx={{ flex: 1, overflow: 'auto', p: 2 }}>
        <Container maxWidth="md">
          {messages.map((message, index) => (
            <Fade key={index} in={true}>
              <Box sx={{ mb: 3 }}>
                {message.type === 'user' ? (
                  <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
                    <Paper
                      sx={{
                        p: 2,
                        maxWidth: '80%',
                        background: 'linear-gradient(135deg, #6366f1, #4f46e5)',
                        borderRadius: '16px 16px 4px 16px',
                      }}
                    >
                      <Typography
                        component="pre"
                        sx={{
                          fontFamily: '"JetBrains Mono", monospace',
                          fontSize: '0.875rem',
                          whiteSpace: 'pre-wrap',
                          wordBreak: 'break-word',
                          m: 0,
                        }}
                      >
                        {message.content}
                      </Typography>
                    </Paper>
                  </Box>
                ) : (
                  <Box>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
                      <Avatar sx={{ bgcolor: 'primary.main', width: 32, height: 32 }}>
                        <AIIcon fontSize="small" />
                      </Avatar>
                      <Typography variant="subtitle2" color="text.secondary">
                        AI Test Engineer
                        {message.note && (
                          <Chip
                            size="small"
                            label={message.note}
                            color="warning"
                            variant="outlined"
                            sx={{ ml: 1, height: 20, fontSize: '0.65rem' }}
                          />
                        )}
                      </Typography>
                    </Box>

                    {/* Test Cases */}
                    {message.testCases.length > 0 && (
                      <Box sx={{ mb: 3 }}>
                        <Typography variant="h6" gutterBottom fontWeight="600">
                          Test Cases ({message.testCases.length})
                        </Typography>
                        <Stack spacing={2}>
                          {message.testCases.map((tc, i) => (
                            <TestCaseCard key={i} testCase={tc} />
                          ))}
                        </Stack>
                      </Box>
                    )}

                    {/* pytest Code */}
                    {message.pytestCode && (
                      <Box sx={{ mt: 3 }}>
                        <Box
                          sx={{
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'space-between',
                            mb: 1,
                          }}
                        >
                          <Typography variant="h6" fontWeight="600">
                            Automation Code (pytest)
                          </Typography>
                          <Button
                            size="small"
                            startIcon={copied ? <CheckIcon /> : <CopyIcon />}
                            onClick={() => copyToClipboard(message.pytestCode)}
                          >
                            {copied ? 'Copied!' : 'Copy'}
                          </Button>
                        </Box>
                        <CodeBlock code={message.pytestCode} />
                      </Box>
                    )}

                    {/* Export Button */}
                    <Box sx={{ mt: 2, display: 'flex', justifyContent: 'flex-end' }}>
                      <Button
                        variant="outlined"
                        size="small"
                        startIcon={<DownloadIcon />}
                        onClick={exportAll}
                      >
                        Export All
                      </Button>
                    </Box>
                  </Box>
                )}
              </Box>
            </Fade>
          ))}
          <div ref={messagesEndRef} />
        </Container>
      </Box>

      {/* Loading Indicator */}
      {loading && (
        <Container maxWidth="md" sx={{ mb: 2 }}>
          <Paper sx={{ p: 2, display: 'flex', alignItems: 'center', gap: 2 }}>
            <LinearProgress sx={{ flex: 1 }} />
            <Typography variant="caption" color="text.secondary">
              Generating test cases...
            </Typography>
          </Paper>
        </Container>
      )}

      {/* Input Area */}
      <Paper
        elevation={4}
        sx={{
          p: 2,
          background: 'rgba(30, 41, 59, 0.95)',
          backdropFilter: 'blur(10px)',
          borderTop: '1px solid rgba(255,255,255,0.1)',
        }}
      >
        <Container maxWidth="md">
          <Box sx={{ display: 'flex', gap: 1 }}>
            <TextField
              fullWidth
              multiline
              maxRows={6}
              placeholder="Paste your Python code or feature description here... (Ctrl+Enter to send)"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              inputRef={inputRef}
              disabled={loading}
              sx={{
                '& .MuiOutlinedInput-root': {
                  fontFamily: '"JetBrains Mono", monospace',
                  bgcolor: 'background.paper',
                  borderRadius: 2,
                },
              }}
            />
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
              <Tooltip title="Send (Ctrl+Enter)">
                <span>
                  <Fab
                    color="primary"
                    size="medium"
                    onClick={handleSend}
                    disabled={!input.trim() || loading}
                  >
                    <SendIcon />
                  </Fab>
                </span>
              </Tooltip>
              {input && (
                <Tooltip title="Clear">
                  <IconButton size="small" onClick={() => setInput('')} color="error">
                    <ClearIcon />
                  </IconButton>
                </Tooltip>
              )}
            </Box>
          </Box>
          <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block', textAlign: 'center' }}>
            Tip: Paste Python code for detailed tests, or describe features for manual test cases
          </Typography>
        </Container>
      </Paper>

      {/* Error Snackbar */}
      <Snackbar
        open={!!error}
        autoHideDuration={6000}
        onClose={() => setError(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert severity="error" onClose={() => setError(null)}>
          {error}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default ChatPage;
