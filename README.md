# Backend

This folder contains a small Flask API.

Quick start (PowerShell):

1. Run the helper script to create a venv, install requirements, and start the server:

```powershell
cd "$(Split-Path -Path $MyInvocation.MyCommand.Definition -Parent)"
.\start-backend.ps1
```

Manual commands (PowerShell):

```powershell
cd "C:\Users\Yolanda S'phesihle M\Documents\simple API frontend\Backend"
python -m venv venv
.\venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe app.py
```

Test the `/calculate` endpoint (PowerShell):

```powershell
Invoke-RestMethod -Method POST -Uri http://127.0.0.1:5000/calculate -ContentType 'application/json' -Body '{"num1":4,"num2":2,"operation":"multiply"}'
```

Or with `curl`:

```powershell
curl -X POST http://127.0.0.1:5000/calculate -H "Content-Type: application/json" -d '{"num1":4,"num2":2,"operation":"multiply"}'
```
