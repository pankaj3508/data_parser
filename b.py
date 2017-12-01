import requests
from bs4 import BeautifulSoup
url="https://www.gsmarena.com/acer-phones-59.php";
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
classname=soup.find(class_="makers")
a=classname.find_all('a')
for link in a:
	print(link.get('href'))
url2="https://www.gsmarena.com/"
classname2=soup.find(class_="nav-pages")
a2=classname2.find_all('a')
for link in a2:

	url3=url2
	url3=url3+link.get('href')

	print(url3+"\n\n")
	page=requests.get(url3)
	soup2=BeautifulSoup(page.content,'html.parser')
	classname3=soup2.find(class_="makers")
	a=classname3.find_all('a')
	for link in a:
		print(link.get('href'))
