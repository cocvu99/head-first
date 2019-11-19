Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
	["Graham Chapman",
		 ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
		  "Terry Jones"]]]
>>> 
>>> for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			print(nested_item)
	else:
		print(each_item)

The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
>>> 
>>> for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else
	
SyntaxError: invalid syntax
>>> for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)

The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones
>>> 
