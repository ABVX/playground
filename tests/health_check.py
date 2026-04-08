import subprocess
import requests
import datetime
import os
import time
from dotenv import load_dotenv

load_dotenv("../.env")

TOKEN = os.getenv("TG_TOKEN")
ID = os.getenv("TG_CHAT_ID")
URL = "http://localhost:8080"
CONTAINER_NAME = "remote-archiver"
LOG_FILE = "/home/vlad/Desktop/archiver/app.log"

def send_tg(message1):
    if not TOKEN or not ID:
        print("Error: Token of Chat id not found in .env")
        return
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": ID, "text": message1}
        requests.post(url, data=data, timeout=5)
    except Exception as e:
        print(f"Failed to send telegram: {e}")

def log_message(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open (LOG_FILE, "a") as  f:
        f.write(f"[{timestamp}] {msg}\n")

def check_service():
    print(f"--- Checking {CONTAINER_NAME} --- ")

    result = subprocess.run(["docker", "inspect", "-f", "{{.State.Running}}", CONTAINER_NAME],
                            capture_output=True, text=True)

    if "true" not in result.stdout:
        msg = "CRITICAL: Container is NOT running. Attemping to start..."
        log_message(msg)
        send_tg(msg)

        subprocess.run(["docker","start", CONTAINER_NAME])
        time.sleep (5)

        check_again = subprocess.run(["docker", "inspect", "-f", "{{.State.Running}}", CONTAINER_NAME],
                                     capture_output=True, text=True)

        if "true" in check_again.stdout:
              msg_up = f"Fixed: Container {CONTAINER_NAME} is now up and running."
              log_message(msg_up)
              send_tg(msg_up)
        return True
    else:
        msg_fail = f"Failed to start container {CONTAINER_NAME}."
        log_message(msg_fail)
        send_tg(msg_fail)
        return False

    try:
        response = requests.get(URL, timeout=3)
        if response.status_code == 200:
            msg = "INFO: 200 OK"
            return True

        else:
            msg = f"WARNING: Service returned status {response.status_code}"
            log_message(msg)
            send_tg(msg)
            return False

    except Exception as e:
        msg = f"ERROR: Could not connect to service: {e}"
        log_message(msg)
        send_tg(msg)
        return False

if __name__ == "__main__":
    if check_service():
        print("Status: OK")
    else:
        print("Status:ERROR (Check app.log)")
