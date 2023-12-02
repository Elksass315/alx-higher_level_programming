#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
