# React Frontend - Test Case Generator

Modern React frontend with Material-UI for the Local Test Case Generator.

## Features

- **Material-UI Components** - Beautiful, modern UI components
- **Dark Theme** - Professional dark mode interface
- **Syntax Highlighting** - Code display with PrismJS
- **Responsive Design** - Works on desktop and mobile
- **Real-time Feedback** - Loading states and error handling

## Quick Start

### Prerequisites
- Node.js 16+ 
- npm or yarn

### Installation

```bash
cd Project1-LocalTestCaseGenerator/frontend
npm install
```

### Development Mode

```bash
npm start
```

This will start the React development server on `http://localhost:3000`

**Note:** The Flask backend should be running on `http://localhost:5000`

### Build for Production

```bash
npm run build
```

This creates a `build` folder with optimized files. The Flask backend will automatically detect and serve these files.

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── TestCaseCard.js    # Test case display component
│   │   └── CodeBlock.js       # Code syntax highlighting
│   ├── pages/
│   │   └── ChatPage.js        # Main chat interface
│   ├── services/
│   │   └── api.js             # API communication
│   ├── App.js                 # Main app component
│   └── index.js               # Entry point
├── package.json
└── README.md
```

## Usage

1. Start Flask backend:
   ```bash
   cd Project1-LocalTestCaseGenerator
   python deploy.py
   ```

2. Start React frontend (in new terminal):
   ```bash
   cd Project1-LocalTestCaseGenerator/frontend
   npm start
   ```

3. Open browser to `http://localhost:3000`

## Build and Deploy

To use the React frontend with Flask:

```bash
# Build React app
cd frontend
npm run build

# Start Flask (it will auto-detect the build folder)
cd ..
python deploy.py
```

The Flask server will now serve the React app from the `build` folder.

## Technologies Used

- React 18
- Material-UI (MUI) v5
- Axios
- PrismJS (syntax highlighting)
