import requests

url = "https://httpbin.org/put"

data = {
    "name" : "Jai",
    "city" : "Mumbai"
}

response = requests.put(url, json=data)

print(response.status_code)
print(response.text)