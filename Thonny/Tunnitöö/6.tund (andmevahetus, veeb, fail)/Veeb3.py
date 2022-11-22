from webbrowser import *
open("www.cs.ut.ee")

print()

# from webbrowser import *
# aadress = "http://www.eki.ee/dict/qs/index.cgi?Q=programmeerimine"
# open (aadress)

# print()

from webbrowser import *
sona = input("Sisestage sõna: ")
aadress = "http://www.eki.ee/dict/qs/index.cgi?Q=" + sona
open(aadress)