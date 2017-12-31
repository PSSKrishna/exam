#!/usr/bin/python

# print date in every 10 sec using crontab :
# crontab -e 
# * * * * * /usr/bin/python /root/date_try.py	>> /root/date.txt

import os,time

t=0
while(t<6):
	time.sleep(10)
	os.system('date')
	t=t+1


