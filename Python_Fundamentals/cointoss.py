import random
maximum = 5000

def cointoss(maximum):
	headcount = 0
	tailcount = 0
	for i in range (1, maximum + 1):
		random_num = random.random()
		random_rounded = round (random_num)
		if random_rounded == 0:
			headcount += 1
			print "Attempt #" + str(i) + ": Throwing a coin... It's heads! ... Got " + str ( headcount ) + " head(s) so far and " + str(tailcount) + " tail(s) so far"
		else:
			tailcount += 1
			print "Attempt #" + str(i) + ": Throwing a coin... It's tails! ... Got " + str ( tailcount ) + " tail(s) so far and " + str(headcount) + " head(s) so far"		
	print "ending"

cointoss( maximum )