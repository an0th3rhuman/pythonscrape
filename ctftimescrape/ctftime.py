import requests
from bs4 import BeautifulSoup as bs
import smtplib
url = "https://ctftime.org/event/list/?year=2017&online=1&format=1&restrictions=0&upcoming=true"
r = requests.get(url)
soup = bs(r.content)
ctfdata = soup.find_all("table",{"class":"table table-striped"})

for items in ctfdata:
    scraped = items.text
print scraped


