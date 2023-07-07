#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
with `requests` module
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)

