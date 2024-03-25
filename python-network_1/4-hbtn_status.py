#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""

import requests

url = 'https://intranet.hbtn.io/status'
response = requests.get(url)

print("Body response:")
print("\t- type:{}", format(type(response.text).__name__))
print("\t- content:{}", format(response.text))
