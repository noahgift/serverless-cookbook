import requests

url = "https://us-central1-cloudai-194723.cloudfunctions.net/change722"
payload = {"amount": 1.34}
result = requests.post(url, data=payload)
print(result.text)
