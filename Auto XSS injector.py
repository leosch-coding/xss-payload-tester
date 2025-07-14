import time
import random
import urllib
from urllib.parse import parse_qs
from urllib import request, error
URL = input("Enter first URL here:")
param = input("Enter Parameters here:")
method = input("GET/POST:")

with open("XSS payloads.txt", "rt") as f:
    payloads = [line.strip() for line in f if line.strip()]

headers= {"User-Agent": "BugBountyTestingBot/1.0 (contact:lhrs@wearehackerone.com)"}
for payload in payloads:
    encoded_payload = urllib.parse.quote(payload)
    GET_method = "GET"
    POST_method = "POST"
    res = ""
    if method == GET_method:
        try:
            url = f"{URL}?{param}={encoded_payload}"
            req = urllib.request.Request(url, headers=headers)
            with request.urlopen(req, timeout=10) as res:
                res_body = res.read().decode()
                print(res_body)
                time.sleep(random.uniform(1, 3))
        except error.HTTPError as e:
                print("HTTP Error", e.code)
                continue


    if method == POST_method:
        try:
            data = urllib.parse.urlencode({param:payload}).encode()
            req = urllib.request.Request(URL, data=data, headers=headers)
            with request.urlopen(req, timeout=10) as res:
                res_body = res.read().decode()
                print(res_body)
                time.sleep(random.uniform(1, 3))
        except error.HTTPError as e:
            print("HTTP Error", e.code)
            continue


    if payload in res_body:
        print("Payload Reflected! Possible XSS!")



