from steem import Steem
import re

s=Steem()

following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine','a','blog',1000)))
inc=0
following=[]
for i in following_:
	following.append(i)
while inc==0:
	if len(following_)==1000:
		x=following_[-1]
		following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',x,'blog',1000)))
		for i in following_:
			if i not in following:
				following.append(i)
	else:
		x=following_[-1]
		following_=re.findall("'following': '(.+?)'",str(s.get_following('digital.mine',x,'blog',1000)))
		for i in following_:
			if i not in following:
				following.append(i)
		inc=1

file=open('all_followed.txt','r')
al_=file.readlines()
al=[]

for i in al_:
	if '\n' in i:
		i=i.replace('\n','')
		al.append(i)
file.close()
file=open('all_followed.txt','a')
for i in following:
	if i not in al:
		file.write(i+'\n')

print ('FILE with',len(al_))		
print ('FILE without',len(al))
print ('ACTUAL FOLLOWING',len(following))
