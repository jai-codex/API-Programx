import requests

url = "https://httpbin.org/delete"

response = requests.delete(url)

print(response.status_code)
print(response.text)