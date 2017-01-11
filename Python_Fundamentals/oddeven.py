def oddeven(maximum):
	for number in range(1,maximum + 1):
		if number % 2 == 0:
			print "Number is " + str(number) + ". This is an even number."
		else: 
			print "Number is " + str(number) + ". This is an odd number."

oddeven(2000)