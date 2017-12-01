import requests
from bs4 import BeautifulSoup
url="https://www.gsmarena.com/makers.php3";
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
classname=soup.find(class_="st-text")
td=soup.find_all('td')
a=classname.find_all('a')
for link in a:
	print(link.get('href'))
