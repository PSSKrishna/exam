#!/usr/bin/python

#find input type integer,alpha,alphanumeric

a = raw_input()
if a.isdigit():
	print "integer"
elif a.isalpha():	
	print "string"
else:
	print "alphanumeric"
