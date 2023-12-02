#!/usr/bin/python3
"""fetche https://alx-intranet.hbtn.io/status using urllib"""


if __name__ == "__main__":
    import urllib.request
    import sys

    if len(sys.argv) == 2:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.headers.get('X-Request-Id'))
