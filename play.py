#!/usr/bin/python
import os
import re


mp3=[]
search_res=[]
s=0
mount_point=raw_input('Enter mount point')
drive_walk=os.walk(mount_point)
all_drives=[os.path.join(mount_point, i) for i in drive_walk.next()[1]]
print 'Mounted Drives Found are:'
for i in all_drives:
	print i
print "Total: %d"%len(all_drives)

print "########Seaching songs ..#########" 
for l in all_drives:
	dirs=os.walk(l)
	print ". . .",
	for d in dirs:
		
     		for f in d[2]:
             		if re.search('.mp3$',f):
             			mp3.append((d[0]+'/',f))                     
 
print "########Total songs found:%d"%len(mp3)
while s!='e':
	
	
	if s=='s':
		search_res=[]
		fav=raw_input('enter search')
		for f_se in mp3:
			if re.search(fav.lower(),f_se[1].lower()):
				search_res.append(f_se)
	elif s=='r':
		search_res=[]
		o=open('playlist.pli','r')
		for p in o:
			search_res.append(tuple(p[:len(p)-1].split('!@#$%^&*')))
		o.close()
		search_res=list(set(search_res))
	elif s=='c':
                ftip=raw_input('Enter the ftp address of the target device') 
		for f in search_res:
			
			print "###Copying "+f[1],
			os.system('wput \"'+f[0]+f[1]+'\" \"'+ftip+'music/Mtranfers/'+f[0]+'\">dump')
			print "Done!."
	s='0'

	
	print "########Total songs found after search:%d"%len(search_res)
	while s!='s' and s!='e' and s!='r'and s!='c':

		c=0
		for f in search_res:
			print "-"*80
			f_print=str(c)+' | '+f[1]
			
			print f_print+" "*(80-len(f_print))+"|"
			
			c=c+1
		print "-"*80
		print 's | search'+" "*(80-10)+"|"
		print "-"*80
		print 'e | exit'+" "*(80-8)+"|"
		print "-"*80
		print 'r | recent'+" "*(80-10)+"|"
		print "-"*80
		print 'c | copy all recent to phone'+" "*(80-28)+"|"
		print "-"*80
		s=raw_input('select an option')
		#os.system('clear')
 	
		if s!='e' and s!='s' and s!='r'and s!='c':
			o=open('playlist.pli','a')
			o.write(search_res[int(s)][0]+'!@#$%^&*'+search_res[int(s)][1]+'\n')
			o.close()
				
			print "#######Playing the song %s##########Enjoy"%search_res[int(s)][1]
			os.system('cvlc -q --play-and-exit \"'+search_res[int(s)][0]+search_res[int(s)][1]+'\"')
			print "#######Stopped #########"
	

