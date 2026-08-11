import requests

username = "kumbharvivek93-cmyk"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
print(response.status_code)
data = response.json()

print(data["login"])
print(data["public_repos"])
print(data["followers"])