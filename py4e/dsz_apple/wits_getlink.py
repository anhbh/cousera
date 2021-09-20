import os,re,ssl

import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE


url='http://wits.dzsi.net/browse/V2724X-1307'

content=urllib.request.urlopen(url,context=ctx).read().decode()
soup=BeautifulSoup(content,'html.parser')

