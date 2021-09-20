import urllib.request, urllib.parse, urllib.error
import os, re, ssl

#os.chdir('D:\\OneDrive - DZS\\03-Courses\\04-Python\\code3')

from bs4 import BeautifulSoup


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url='http://apple.dzsi.net/tftpboot/V2724GG/2.05/dump/'


content=urllib.request.urlopen(url,context=ctx) 
soup=BeautifulSoup(content,'html.parser')

# parsing the soup
tag=soup.table
print(tag)
#for tag in tags:
#	print(tag.name)




#tables=soup.find_all('table')
#tds=soup.find_all('td')

# file list
#for td in tds:
#	print(str(td))
#	tmp=str(td).split('\"')
#	if len(tmp)<8: continue
#	print('File name: ',tmp[3])
	