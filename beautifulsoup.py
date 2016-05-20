#! /usr/bin/python
import urllib
from bs4 import BeautifulSoup
url= "http://"
ht= urllib.urlopen(url)
html_page= ht.read()
b= BeautifulSoup(html_page,"lxml")
data = b.find('div',id = 'notice')
print data
