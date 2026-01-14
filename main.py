import requests

print("Olá, mundo!")

response = requests.get("https://api.github.com")
print("Status da requisição:", response.status_code)
