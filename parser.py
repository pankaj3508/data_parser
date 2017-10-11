import requests
from bs4 import BeautifulSoup
url="http://www.allindiaexams.in/aptitude-questions-and-answers/problems-on-trains/";
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#html=list(soup.children)
#body=list(html.children)
#list(body.children)......and so on to the hierarchy
#body.get_text()
questions=soup.find_all(class_="qa_list")

ques_list=[]
option1=[]
option2=[]
option3=[]
option4=[]
explanation=[]

answer=soup.find_all(class_="answer")
ans_list=[]
i=0
for ans in answer:
	ss=ans.get_text()
	ss=ss[4:]
	ans_list.insert(i,ss)
	i=i+1

file=open("questions","a+")
i=0;
for ques in questions:
	s=ques.get_text()
	for i in range(0,len(s)):
		if(s[i]=='\n'):
			pos1=i
		elif(s[i]=='\t'):
			pos2=i
			break;
	que=s[pos1+3:pos2]
	ques_list.insert(i,que)
	s=s.replace(que+'\t','')
	for i in range(3,len(s)):
		if(s[i]=='\t'):
			pos1=i;
		elif(s[i]=='\n'):
			pos2=i;
			break;
	opt1=s[pos1+5:pos2]
	option1.insert(i,opt1)
	s=s.replace(opt1+'\n','')
	s=s[9:]
	for i in range(0,len(s)):
		if(s[i]=='\n'):
			pos2=i;
			break;
	opt2=s[3:pos2]
	option2.insert(i,opt2)
	s=s.replace(s[0:pos2+5],'')
	for i in range(0,len(s)):
		if(s[i]=='\n'):
			pos2=i
			break;
	opt3=s[0:pos2]
	option3.insert(i,opt3)
	s=s.replace(s[0:pos2+5],'')
	for i in range(0,len(s)):
		if(s[i]=='\n'):
			pos2=i
			break;
	opt4=s[0:pos2]
	option4.insert(i,opt4)
	pos1=s.find("Explanation:")
	pos2=s.find("Workspace",pos1)
	exp=s[pos1+14:pos2-5]
	explanation.insert(i,exp)
	i=i+1
	#print(exp)

	#print(opt1)

for i in range(0,len(option1)-1):
	file.write(ques_list[i]+'\n')
	file.write(option1[i]+'\n')
	file.write(option2[i]+'\n')
	file.write(option3[i]+'\n')
	file.write(option4[i]+'\n')
	file.write(ans_list[i]+'\n')
	file.write("Explanation:"+'\n')
	file.write(explanation[i]+'\n')






































