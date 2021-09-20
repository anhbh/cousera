# chapter 11 - retry assignment

import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url='http://py4e-data.dr-chuck.net/comments_1349622.xml'

data=urllib.request.urlopen(url, context=ctx).read()

print(data.decode())

tree = ET.fromstring(data)

comments=tree.findall('comments')
comment_list=comments[0].findall('comment')

total = 0

for comment in comment_list:
	count= comment.find('count').text
	name= comment.find('name').text
	print('Name:', name, 'Count:', count)
	total += int(count)
	
print('Total:',total)