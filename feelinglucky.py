#!python3
#feeling lucky.py, it opens several google search results

import requests, sys, webbrowser, bs4

print('googling...')
res = requests.get('http://www.google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.content,'lxml')#different from the book

linkElements = soup.select('.r a')

numOpen = min(5,len(linkElements))
for i in range(numOpen):
	webbrowser.open('http://www.google.com'+linkElements[i].get('href'))
