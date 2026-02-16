import requests

url = "https://google.com"
response = requests.get(url)

with open("index.html", "w") as f:
	f.write(response.text)

print(response.status_code)
print("OK")
