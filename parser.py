import requests
from bs4 import BeautifulSoup
url="http://www.allindiaexams.in/aptitude-questions-and-answers/problems-on-trains/2";
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#html=list(soup.children)
#body=list(html.children)
#list(body.children)......and so on to the hierarchy
#body.get_text()
questions=soup.find_all(class_="qa_list")

ques_list=[]


file=open("questions","a+")
for ques in questions:
	s=ques.get_text()+"\n"
	file.write(s)


