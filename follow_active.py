from steem import Steem
import time
import re
import all_followed_list
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
file=open('active_acc.txt','r')
al=file.readlines()
file.close()
active=[]
fol=[]
for i in al:
	if '\n' in i:
		i=i.replace('\n','')
		active.append(i)
###
file=open('all_followed.txt','r')
al_=file.readlines()
file.close()
for i in al_:
	if '\n' in i:
		i=i.replace('\n','')
		if i not in following:
			following.append(i)
	
###		
			
counter=0
count=1
print (len(active))
while len(active)>0:
	for i in active:
		if i not in following:
			try:
				s.follow(i)
				active.remove(i)
				fol.append(i)
				counter+=1
			except Exception :
				pass
				print ('FAILED')
		
		if counter==15:
			print ('ROUND',count)
			print ('FOLLOWED 15')
			print (len(active), 'TO GO')
			print (len(fol), 'TOTAL FOLLOWED')
			print ('__________________________')
			counter=0
			count+=1
			time.sleep(3600)
