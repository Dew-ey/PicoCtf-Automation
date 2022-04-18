import pwn
import re

def main():
    from pwn import remote
    url = "jupiter.challenges.picoctf.org"
    port = "4427"
    r = remote(url,port)
    output = r.recvall().decode()
    flag = re.findall(r"picoCTF{.*?}", output)[0]
    print(flag)
main()