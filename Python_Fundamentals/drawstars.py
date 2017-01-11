x = [4,"Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(list):
	for object in list:
		if type(object) == int:
			stars = ""
			for i in range(0,object):
				stars += "*"
			print stars
		if type(object) == str:
			name = ""
			for i in range(0,len(object)):
				name+= object[0].lower()
			print name

draw_stars(x)