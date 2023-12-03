#!/usr/bin/python3
"""script that send email using requests package"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
    except Exception as e:
        print(str(e))
