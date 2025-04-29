import requests

HOST = "10.0.2.15"               
URL = f"http://{HOST}"

try:
    resp = requests.head(URL, timeout=5)
except Exception as e:
    print(f"Error connecting to {HOST}: {e}")
    exit(1)

print("Server:", resp.headers.get("Server", "Not present"))
print("X-Frame-Options:", resp.headers.get("X-Frame-Options", "Not present"))
print("X-Content-Type-Options:", resp.headers.get("X-Content-Type-Options", "Not present"))
