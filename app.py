from flask import Flask
import requests

app = Flask(__name__)

print("archiver is running")

def download_page():
    url = "https://google.com"
    response = requests.get(url)

    with open("index.html", "w") as f:
        f.write(response.text)

@app.route('/')
def hello():
    download_page()
    return "Status OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
