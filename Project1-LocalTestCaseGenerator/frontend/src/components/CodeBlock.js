import React, { useEffect, useRef } from 'react';
import { Paper, Typography, Box } from '@mui/material';
import Prism from 'prismjs';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism-tomorrow.css';

const CodeBlock = ({ code }) => {
  const codeRef = useRef(null);

  useEffect(() => {
    if (codeRef.current) {
      Prism.highlightElement(codeRef.current);
    }
  }, [code]);

  return (
    <Paper
      variant="outlined"
      sx={{
        overflow: 'hidden',
        borderRadius: 2,
        border: '1px solid rgba(255,255,255,0.1)',
      }}
    >
      <Box
        sx={{
          px: 2,
          py: 1,
          background: 'rgba(0,0,0,0.3)',
          borderBottom: '1px solid rgba(255,255,255,0.1)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <Typography variant="caption" color="text.secondary">
          test_generated.py
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Python
        </Typography>
      </Box>
      <Box
        sx={{
          background: '#1d1f21',
          overflow: 'auto',
          maxHeight: '400px',
        }}
      >
        <pre
          style={{
            margin: 0,
            padding: '16px',
            fontSize: '0.875rem',
            fontFamily: '"JetBrains Mono", "Fira Code", monospace',
            lineHeight: 1.5,
          }}
        >
          <code ref={codeRef} className="language-python">
            {code}
          </code>
        </pre>
      </Box>
    </Paper>
  );
};

export default CodeBlock;
