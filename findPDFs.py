from bs4 import BeautifulSoup
import requests
import sys

response = requests.get(sys.argv[1])

soup = BeautifulSoup(response.text)
for links in soup.find_all('a'):
    href = links.get('href')
    r = requests.get(href)
    if r.headers['Content-Type'] == 'application/pdf':
        print ("URI: {}".format(r.url))
        print ("Final URI: {}".format(r.request.url))
        print ("Content Length: {}\n".format(r.headers['Content-Length']))
