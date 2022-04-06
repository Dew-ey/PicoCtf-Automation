import requests
import re

def main():
    url = "https://jupiter.challenges.picoctf.org/problem/28921/flag"
    header = {
        "User-Agent": "picobrowser"
    }
    r = requests.get(url,headers=header)
    flag = re.findall(r'picoCTF{.*?}', r.text)[0]
    print(flag)

main()