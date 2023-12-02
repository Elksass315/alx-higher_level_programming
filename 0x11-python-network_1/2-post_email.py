#!/usr/bin/python3
"""send email using urllib"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        data = urllib.parse.urlencode({'email': email})
        data = data.encode('ascii')
        with urllib.request.urlopen(url, data) as response:
            print(response.read().decode('utf-8'))
