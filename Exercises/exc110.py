import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print("It is not possible access 'pudim' site's, sorry.")
else:
    print("'Pudim' site's is accessible!")
