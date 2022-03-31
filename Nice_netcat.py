import pwn
import re


def main():
    from pwn import remote
    
    url = "mercury.picoctf.net"
    port = 22902 
    #gives a stored url and port
    #assgins remote connection for given url and port
    r = remote(url,port)
    #assgins varible output to the decoded and recived lines
    output = r.recvall().decode()

    #casts code from decimal to readable ascii
    flag = ""
    for i in output.split():
        flag += chr(int(i)) #parses through list and translates values first to int then to characters and presents in readable format
    print(flag)


main()
