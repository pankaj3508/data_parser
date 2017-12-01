import requests
from bs4 import BeautifulSoup
url="https://www.gsmarena.com/acer_iconia_tab_10_a3_a40-8080.php#";
page=requests.get(url)
soup=BeautifulSoup(page.content,'lxml')
classname=soup.find(id="specs-list")
table=classname.find_all('table')
for tb in table:
	tr=tb.find_all('tr')
	for trr in tr:
		th=trr.find('th')
		if(th):
			print(th.get_text())
		td=trr.find_all('td')
		for tdd in td:
			print(tdd.get_text())
	print("\n")
			
		
	
	

