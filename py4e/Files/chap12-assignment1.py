# chapter 12 - assignment 1


import urllib.request, urllib.parse, urllib.error
import ssl, json


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url='http://py4e-data.dr-chuck.net/comments_1349623.json'

connection=urllib.request.urlopen(url, context=ctx)
data=connection.read().decode()

try:
    js=json.loads(data)
except:
    print(" Can't retrieving json data")
    exit()
    
comments=js['comments']
print("Retrieved", len(comments), "entries")

total=0
for comment in comments:
    count=comment['count']
    total+=count
    
print('Total:',total)