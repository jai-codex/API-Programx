import requests

try:
    url = "https://httpbin.org/delete"

    response = requests.delete(url)

    print(response.status_code)
    print(response.text)
    
except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.") 