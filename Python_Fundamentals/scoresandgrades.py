def scoresandgrades():
	for i in range(0, 10):
		score = input("Enter a score 0-100:")
		if score > 60 and score < 70:
			print "Score: " + str(score) + "; Your grade is D"
		elif score > 69 and score < 80:
			print "Score: " + str(score) + "; Your grade is C"
		elif score > 79 and score < 90:
			print "Score: " + str(score) + "; Your grade is B"
		elif score > 89 and score < 101:
			print "Score: " + str(score) + "; Your grade is A"
	print "End of the program. Bye!"

scoresandgrades()