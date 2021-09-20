# Chapter 11 - Assignment 1

# url
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url='http://py4e-data.dr-chuck.net/comments_1349622.xml'

data=urllib.request.urlopen(url,context=ctx).read()

print(data.decode())
tree=ET.fromstring(data)

gcomments=tree.findall('comments')
comments=gcomments[0].findall('comment')

total=0

for comment in comments:
    count=comment.find('count').text
    print(count)
    total += int(count)

print('Total:', total)




