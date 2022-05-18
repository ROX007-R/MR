#Author MR.RAKIB.404

import os, platform
os.system('git pull')
try:os.system('mr ok')
except:pass
try:os.system('mr cp')
except:pass
try:

   import requests

except:

   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from mking64 import*
    menu().main()
elif bit == '32bit':
    from mking32 import*
    menu().main()
