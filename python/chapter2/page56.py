Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
	["Graham Chapman",
		 ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
		  "Terry Jones"]]]
>>> import nester
>>> print_lol(movies, 0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print_lol(movies, 0)
NameError: name 'print_lol' is not defined
>>> def print_lol(the_list, level):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			for tab_stop in range(level):
				print("\t", end=")
				      
SyntaxError: EOL while scanning string literal
>>> def print_lol(the_list, level):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			for tab_stop in range(level):
				print("\t", end='')
			print(each_item)

>>> print_lol(movies, 0)
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print_lol(movies, 0)
  File "<pyshell#12>", line 4, in print_lol
    print_lol(each_item)
TypeError: print_lol() missing 1 required positional argument: 'level'
>>> 
