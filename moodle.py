#AUTHOR-ROHITH.K

import requests
from bs4 import BeautifulSoup
import os


name = input('enter your username:')
password = input('enter the password:')
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
get_url  ='https://moodle.reva.edu.in/moodle/'
post_url = 'https://moodle.reva.edu.in/moodle/login/index.php'
payload = {
'username': name,
'password': password
}


s = requests.session()
r = s.get(get_url,headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
payload['logintoken'] = soup.find('input', attrs={'name': 'logintoken'})['value']
post = s.post(post_url,data=payload)
soup2 = BeautifulSoup(post.content,'html5lib')

result = soup2.select("div.event")
with open('upcoming events.txt','w')as f:
    for i in result:
        print(i.text,file=f)

file = 'upcoming events.txt'

if os.stat(file).st_size == 0:
    print('parse unsuccessful..please check your credentials')
else:
    print('parse completed...your file is saved as '+file+' in document folder')


