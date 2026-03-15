import requests

def archiver_test():
    url = "http://localhost:8080"

    try:
        response = requests.get(url)
        assert response.status_code == 200
        print("First test success")

    except Exception as e:
        print(f"Test failed!: {e}")

if __name__ == "__main__":
    archiver_test()
