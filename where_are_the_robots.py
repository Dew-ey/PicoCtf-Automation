import requests
import re


url = "http://jupiter.challenges.picoctf.org:56830/1bb4c.html"


r = requests.get(url)


flag = re.findall(r'picoCTF{.*?}', r.text)[0]
print(flag)

