import React from 'react';
import { Card, CardContent, Typography, Chip, Box, Stack } from '@mui/material';
import { CheckCircle as PositiveIcon, Cancel as NegativeIcon, Info as InfoIcon } from '@mui/icons-material';

const TestCaseCard = ({ testCase }) => {
  const { id, title, type, steps, expected } = testCase;

  const getTypeColor = () => {
    switch (type?.toUpperCase()) {
      case 'POSITIVE':
        return 'success';
      case 'NEGATIVE':
        return 'error';
      default:
        return 'default';
    }
  };

  const getTypeIcon = () => {
    switch (type?.toUpperCase()) {
      case 'POSITIVE':
        return <PositiveIcon fontSize="small" />;
      case 'NEGATIVE':
        return <NegativeIcon fontSize="small" />;
      default:
        return <InfoIcon fontSize="small" />;
    }
  };

  return (
    <Card
      variant="outlined"
      sx={{
        borderLeft: 4,
        borderLeftColor: type?.toUpperCase() === 'POSITIVE' ? 'success.main' : 
                        type?.toUpperCase() === 'NEGATIVE' ? 'error.main' : 'primary.main',
        background: type?.toUpperCase() === 'POSITIVE' ? 'success.light' :
                    type?.toUpperCase() === 'NEGATIVE' ? 'error.light' : 
                    'rgba(99, 102, 241, 0.05)',
        '&:hover': {
          transform: 'translateX(4px)',
          transition: 'transform 0.2s',
        },
      }}
    >
      <CardContent>
        <Stack spacing={1.5}>
          {/* Header */}
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 1 }}>
            <Typography
              variant="caption"
              sx={{
                fontFamily: '"JetBrains Mono", monospace',
                color: 'primary.light',
                fontWeight: 600,
              }}
            >
              {id}
            </Typography>
            <Chip
              size="small"
              icon={getTypeIcon()}
              label={type || 'TEST'}
              color={getTypeColor()}
              variant="outlined"
              sx={{ textTransform: 'uppercase', fontSize: '0.65rem', fontWeight: 600 }}
            />
          </Box>

          {/* Title */}
          <Typography variant="subtitle1" fontWeight={600}>
            {title}
          </Typography>

          {/* Steps */}
          {steps && steps.length > 0 && (
            <Box>
              <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', fontWeight: 600 }}>
                Steps:
              </Typography>
              <ol style={{ margin: '4px 0 0 0', paddingLeft: '16px' }}>
                {steps.map((step, index) => (
                  <li key={index}>
                    <Typography variant="body2" color="text.secondary">
                      {step}
                    </Typography>
                  </li>
                ))}
              </ol>
            </Box>
          )}

          {/* Expected Result */}
          {expected && (
            <Box
              sx={{
                p: 1.5,
                borderRadius: 1,
                background: 'rgba(99, 102, 241, 0.1)',
                border: '1px solid rgba(99, 102, 241, 0.2)',
              }}
            >
              <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', fontWeight: 600 }}>
                Expected Result:
              </Typography>
              <Typography variant="body2" sx={{ mt: 0.5 }}>
                {expected}
              </Typography>
            </Box>
          )}
        </Stack>
      </CardContent>
    </Card>
  );
};

export default TestCaseCard;
