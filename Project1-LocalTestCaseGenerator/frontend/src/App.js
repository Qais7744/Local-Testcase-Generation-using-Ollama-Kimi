import React from 'react';
import { Box } from '@mui/material';
import ChatPage from './pages/ChatPage';

function App() {
  return (
    <Box sx={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #020617 0%, #0f172a 100%)',
    }}>
      <ChatPage />
    </Box>
  );
}

export default App;
