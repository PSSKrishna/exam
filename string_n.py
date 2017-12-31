#!/usr/bin/python

a = raw_input()
if a.isdigit():
	print "integer"
elif a.isalpha():	
	print "string"
else:
	print "alphanumeric"
