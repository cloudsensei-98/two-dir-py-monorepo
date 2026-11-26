import requests


def fetch(url: str) -> int:
    resp = requests.get(url, timeout=10)
    return resp.status_code


if __name__ == "__main__":
    print(fetch("https://example.com"))
