import requests

url = "http://127.0.0.1:5000/webhook"
headers = {"Content-Type": "application/json"}
data = {"message": "What is Python?"}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
