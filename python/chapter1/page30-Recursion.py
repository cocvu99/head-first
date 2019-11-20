Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
	["Graham Chapman",
		 ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
		  "Terry Jones"]]]
>>> 
>>> def print_lol(the_list):
	for each_item in the_list:
		if isinstance (each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

>>> print_lol(movies)
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
