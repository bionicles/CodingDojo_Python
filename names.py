users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names(dict):
	
	for type in dict:
		print type

		current = dict.get(type)
		count = 1
		for person in current:
			first = current[(count-1)].get("first_name")
			last = current[(count-1)].get("last_name")
			length = len(first) + len(last)
			print str(count) + " - " + str(first) + " " + str(last) + " - " + str(length)
			count += 1

names(users)