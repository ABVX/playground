from flask import Flask
from service import download_page

app = Flask(__name__)

@app.route('/')
def status():
    download_page()
    return "Status OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
