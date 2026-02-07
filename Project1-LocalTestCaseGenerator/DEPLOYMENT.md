# 🚀 Deployment Guide - BLAST Testcase Generator

## Quick Start (Recommended)

### Option 1: Command Window (Development)
```bash
python run_web.py
```
Access at: http://localhost:5000

### Option 2: Production Server (Fixed Port)
```bash
python deploy.py
```
Access at: 
- http://localhost:5000 (local)
- http://YOUR_IP:5000 (network)

---

## Windows Auto-Start Setup

### Method 1: Simple Batch File (With Window)
1. Double-click `start_server.bat`
2. Server runs on port 5000
3. Press Ctrl+C to stop

### Method 2: Background Service (No Window)
1. Double-click `start_background.vbs`
2. Server runs in background
3. Access at http://localhost:5000

### Method 3: Auto-Start on Windows Boot

#### Step 1: Create Shortcut
1. Right-click `start_background.vbs`
2. Select "Create shortcut"

#### Step 2: Add to Startup
1. Press `Win + R`
2. Type: `shell:startup`
3. Press Enter
4. Copy the shortcut to this folder

Now the server starts automatically every time Windows boots!

---

## Network Access

### Find Your IP Address
```powershell
ipconfig
```
Look for "IPv4 Address" under your active connection.

### Access from Other Devices
Once running with `deploy.py` (host 0.0.0.0), access via:
- http://YOUR_COMPUTER_IP:5000
- http://YOUR_COMPUTER_NAME:5000

Example:
```
http://192.168.1.100:5000
http://DESKTOP-ABC123:5000
```

---

## Custom Port

To run on a different port:

```bash
python deploy.py --port 8080
```

Access at: http://localhost:8080

---

## Running as Windows Service (Advanced)

### Using NSSM (Non-Sucking Service Manager)

1. Download NSSM from https://nssm.cc/
2. Extract and add to PATH
3. Run as Administrator:

```cmd
nssm install BLAST-TestGenerator
```

In the GUI:
- Path: `C:\Path\To\Python\python.exe`
- Arguments: `deploy.py --host 0.0.0.0 --port 5000`
- Startup directory: `C:\Path\To\AITesterBlueprint`

Start the service:
```cmd
nssm start BLAST-TestGenerator
```

---

## Docker Deployment (Optional)

### Build Image
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "deploy.py", "--host", "0.0.0.0"]
```

Build and run:
```bash
docker build -t blast-testgen .
docker run -p 5000:5000 blast-testgen
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find what's using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID)
taskkill /PID <PID> /F

# Or use different port
python deploy.py --port 8080
```

### Firewall Blocking
Allow port 5000 through Windows Firewall:
```powershell
New-NetFirewallRule -DisplayName "BLAST Server" -Direction Inbound -LocalPort 5000 -Protocol TCP -Action Allow
```

### Ollama Not Running
```bash
ollama serve
```

---

## Monitoring

### Check Server Status
```bash
curl http://localhost:5000/api/health
```

### View Logs
Server outputs logs to console. For file logging, modify `deploy.py`.

---

## Summary

| Method | Use Case | Command |
|--------|----------|---------|
| Development | Testing changes | `python run_web.py` |
| Production | Always-on server | `python deploy.py` |
| Background | No cmd window | `start_background.vbs` |
| Auto-start | Boot with Windows | Add to Startup folder |
| Service | System service | Use NSSM |

**Recommended for continuous operation:**
1. Use `deploy.py` for production
2. Use `start_background.vbs` to hide window
3. Add to Startup folder for auto-start
