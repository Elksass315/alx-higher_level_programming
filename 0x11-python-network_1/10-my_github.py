#!/usr/bin/python3
"""using Git hub REST API"""


if __name__ == "__main__":
    import sys
    import requests

    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    data = response.json()
    return data['id']
