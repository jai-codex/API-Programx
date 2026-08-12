import requests

try:
    url = "https://httpbin.org/post"

    data = {
        "name" : "Jai",
        "age" : 19
    }

    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException:
     print("Network error. Please check your internet connection.")     
