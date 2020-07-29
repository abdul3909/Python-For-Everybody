import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_818519.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
data = dict()
tags = soup('span')
add = 0
for tag in tags:
    nmr = tag.contents[0]
    cvr = int(nmr)
    add = cvr + add
print(add)
