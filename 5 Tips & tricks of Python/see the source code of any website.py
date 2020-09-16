#import this

from urllib.request import urlopen

open=urlopen("https://www.python.org/")

print(open.read())

#output : show source code of website
