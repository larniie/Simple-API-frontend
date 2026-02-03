# start-backend.ps1 — creates venv if missing, installs deps, then runs the app
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $scriptDir

$venvPath = Join-Path $scriptDir 'venv'
$pythonVenv = Join-Path $venvPath 'Scripts\python.exe'

if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..."
    & python -m venv $venvPath
    Write-Host "Upgrading pip and installing requirements..."
    & $pythonVenv -m pip install --upgrade pip setuptools wheel
    & $pythonVenv -m pip install -r (Join-Path $scriptDir 'requirements.txt')
}

Write-Host "Starting Flask app..."
& $pythonVenv (Join-Path $scriptDir 'app.py')
