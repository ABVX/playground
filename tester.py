import requests
import sys

def archiver_test():
    url = "http://localhost:8080"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("ALL OK")
            sys.exit(0)
        else:
            print(f"ERROR, CODE: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"NOT WORK: {e}")
        sys.exit(1)

if __name__ == "__main__":
    archiver_test()
