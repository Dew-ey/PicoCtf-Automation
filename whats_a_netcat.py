import pwn
import re



from pwn import remote,context
context.log_level = 'error'

url = "jupiter.challenges.picoctf.org"
port = 41120

r = remote(url,port)#this is how we interact via using remote and passing a url and connection port
output = r.recvall().decode() #decode debugs to ascii string
#regex for picoflags

flag = re.findall(r"picoCTF{.*?}", output)[0]#.* looks for anything in between expressions and ? look for the first exit char

print(flag) #prints whats recived
