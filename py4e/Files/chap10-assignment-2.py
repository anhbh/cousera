# Chapter 10 - Assignment 2

import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import re, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url=input("URL: ")
#pos=input("Position: ")
#rep=input("Repetive: ")

url='http://py4e-data.dr-chuck.net/known_by_Johnny.html'
pos=18
rep=7

res_name=""

def get_url(urlp, posp):
    html=urllib.request.urlopen(urlp,context=ctx).read()
    soup=BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    
    tag=tags[posp - 1]
    res_url=str(re.findall('\"(.*)\"', str(tag))[0])
    res_name=str(re.findall('\>([a-zA-Z]*)\<', str(tag))[0])
    print('url:',res_url,'name:',res_name)
    return (res_url,res_name)
    
for idx in range(0,rep):
    (url,name)=get_url(url,pos)
    res_name = name

print("Result:",name)  