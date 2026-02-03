import subprocess
import time
import sys

python_exe = r"C:\Users\Yolanda S'phesihle M\Documents\simple API frontend\Backend\venv\Scripts\python.exe"
app_path = r"Backend\\app.py"

proc = subprocess.Popen([python_exe, app_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

output = []
start = time.time()
try:
    # read lines as they become available for up to 3 seconds
    while True:
        line = proc.stdout.readline()
        if line:
            output.append(line)
        if time.time() - start > 3:
            break
finally:
    proc.terminate()
    try:
        proc.wait(timeout=2)
    except Exception:
        proc.kill()

print(''.join(output))
