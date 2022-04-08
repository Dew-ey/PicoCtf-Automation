import re
import requests

#uses reqst to an avalible aws to recive the md5hash
def download_files():
    letters = ['a','b']
    for i in letters:
        url = f'https://s3-eu-west-1.amazonaws.com/md5collisions/{i}.php'
        r = requests.get(url)
        files = f'{i}.pdf'
        print(files)
        with open(files, 'wb') as output_file:
            output_file.write(r.content)

def main():
    url = "http://mercury.picoctf.net:50970/index.php"
    md5Inputs = {
        "file1": ('a.pdf', open('a.pdf','rb'), 'application/pdf'),
        "file2": ('b.pdf', open('b.pdf','rb'), 'application/pdf')}
    action = {"submit":"Upload"}
    r = requests.post(url, files=md5Inputs, data=action)
    flag = re.findall("picoCTF{.*?}", r.text)[0]
    print(flag)
download_files()
main()

