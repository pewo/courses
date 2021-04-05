#!/usr/bin/python

largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	try:
		num = int(num)
	except:
		if num == "done" :
			break
		else:
			print "Invalid input"
    
	if num > largest:
		largest = num
	if num < smallest or smallest == None:
		smallest = num

	print "Maximum", largest
	print "Minimum", smallest
