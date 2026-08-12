import requests

url = "https://httpbin.org/post"

data = {
    "name" : "Jai",
    "age" : 19
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())