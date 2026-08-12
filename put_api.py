import requests

try:
    url = "https://httpbin.org/put"

    data = {
        "name" : "Jai",
        "city" : "Mumbai"
    }

    response = requests.put(url, json=data)

    print(response.status_code)
    print(response.text)
except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")     