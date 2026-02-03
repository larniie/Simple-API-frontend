import subprocess
import threading
import time
import urllib.request
import json
import os

venv_python = os.path.join(os.getcwd(), 'Backend', 'venv', 'Scripts', 'python.exe')
app_path = os.path.join('Backend', 'app.py')

proc = subprocess.Popen([venv_python, app_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
lines = []

def reader():
    for line in proc.stdout:
        lines.append(line)
        print(line, end='')

t = threading.Thread(target=reader, daemon=True)
t.start()

# wait for server to start (or timeout)
start_time = time.time()
started = False
while time.time() - start_time < 10:
    if any('Running on' in l or 'Debugger is active' in l for l in lines):
        started = True
        break
    time.sleep(0.2)

if not started:
    print('\nServer did not show startup message within timeout.')

# send POST request
try:
    data = json.dumps({"num1": 4, "num2": 2, "operation": "multiply"}).encode('utf-8')
    req = urllib.request.Request('http://127.0.0.1:5000/calculate', data=data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=5) as resp:
        body = resp.read().decode('utf-8')
        print('\nRESPONSE:', body)
        lines.append('\nRESPONSE: ' + body + '\n')
except Exception as e:
    print('\nPOST ERROR:', e)
    lines.append('\nPOST ERROR: ' + str(e) + '\n')

# give server a moment to log the request
time.sleep(1)

# terminate server
proc.terminate()
try:
    proc.wait(timeout=2)
except Exception:
    proc.kill()

# print a small footer summary
print('\n--- Captured log lines: {} lines ---'.format(len(lines)))
