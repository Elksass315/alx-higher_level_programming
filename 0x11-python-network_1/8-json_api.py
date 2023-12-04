#!/usr/bin/python3
"""script that send email using requests package"""


if __name__ == "__main__":
    import sys
    import requests

    letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data)
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response.get("id"), json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
