Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = [
	"The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
	["Graham Chapman",
		 ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
		  "Terry Jones"]]]
>>> print(movies[4][1][3])
Eric Idle
>>> 
>>> print(movies)
['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
>>> 
>>> for each_item in movies:
	print(each_item)

The Holy Grail
1975
Terry Jones & Terry Gilliam
91
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
>>> 
