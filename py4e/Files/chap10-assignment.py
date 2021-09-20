import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_1349620.html'
handle=urllib.request.urlopen(url, context=ctx)
html=handle.read()
soup=BeautifulSoup(html, 'html.parser')

total=0
tags = soup('span')

for tag in tags:
    print(str(tag), type(tag))
    nums=re.findall('\<span.*>([0-9.]*).*\<\/span\>', str(tag))
    for num in nums:
        total = total + int(num)
    
print("Result:", total)