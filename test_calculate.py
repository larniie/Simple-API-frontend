import json
import urllib.request

url = "http://127.0.0.1:5000/calculate"
payload = {"num1": 4, "num2": 2, "operation": "multiply"}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})

try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        body = resp.read().decode("utf-8")
        print(body)
except Exception as e:
    print("ERROR:", e)
