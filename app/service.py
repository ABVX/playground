import requests
import logging
from config import URL, OUTPUT_FILE

logging.basicConfig(level=logging.INFO)

def download_page():
    try:
        logging.info(f"Downloading: {URL}")
        response = requests.get(URL, timeout=5)
        response.raise_for_status()

        with open(OUTPUT_FILE, "w") as f:
            f.write(response.text)

        logging.info("Saved successfully")

     except requests.RequestException as e:
        logging.error(f:Error downloading page: {e}")

