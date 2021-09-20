import urllib.request, urllib.parse, urllib.error
import os, ssl, re

from bs4 import BeautifulSoup

url='https://www.coursera.org/learn/cs-algorithms-theory-machines/supplement/SNDYI/information-about-lectures-1-10'

content=urllib.request.urlopen(url).read().decode()
soup=BeautifulSoup(content, 'html.parser')
