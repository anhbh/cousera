import urllib.request, urllib.parse, urllib.error
import re, os, ssl

from bs4 import BeautifulSoup


def tag_print(soup, tagname):
	tags=soup.find_all(tagname)
	for tag in tags:
		print(str(tag))

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url='http://infolab.stanford.edu/~backrub/google.html'


html=urllib.request.urlopen(url, context=ctx).read().decode()
soup=BeautifulSoup(html, 'html.parser')
