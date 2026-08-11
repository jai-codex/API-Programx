import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = response.json()

        print("Username:", data["login"])
        print("Public Repositories:", data["public_repos"])
        print("Followers:", data["followers"])
    elif response.status_code == 404:
        print("User not found!")
    else:
        print("Something went wrong.")
        print("Status Code:", response.status_code)     
except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")        
