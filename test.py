import requests

res = requests.post("http://localhost:5000/login")
print(res.json())
