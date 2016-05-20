# Description	: Old school password cracker using python

from sys import platform as _platform

# Check the current operating system to import the correct version of crypt
if _platform == "linux" or _platform == "linux2":
    import crypt 
elif _platform == "darwin":
    # Mac OS X
    import crypt
elif _platform == "win32":
    # Windows
    try:
       import fcrypt # Try importing the fcrypt module
    except ImportError:
       print 'Please install fcrypt  on Windows'



def testPass(cryptPass):	# Start the function
  salt = cryptPass[0:2]
  dictFile=open('/root/Desktop/dic.txt','r')	# Open the dictionary file
  for word in dictFile.readlines():	# Scan through the file
    word=word.strip('\n')
    cryptWord=crypt.crypt(word,salt)	# Check for password in the file
    if (cryptWord == cryptPass):
      print "[+] Found Password: "+word+"\n"
      return
  print "[-] Password Not Found.\n"
  return

def main():
  passFile = open('/root/Desktop/yo.txt')		# Open the password file
  for line in passFile.readlines():	# Read through the file
    if ":" in line:
      user=line.split(':')[0]
      cryptPass = line.split(':')[1].strip(' ') # Prepare the user name etc
      print "[*] Cracking Password For: "+user 
      testPass(cryptPass)				# Call it to crack the users password

if __name__ == "__main__":
  main()
