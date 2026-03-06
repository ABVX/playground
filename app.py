from flask import Flask
import requests

app = Flask(__name__)

print("archiver is running")

@app.route('/')
def hello():
    url = "https://google.com"
    response = requests.get(url)
    with open("index.html", "w") as f:
        f.write(response.text)
    return f"Status: {response.status_code}, OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
