Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def print_lol(the_list, indent=False, level=0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end='')
			print(each_item)

>>> names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
>>> print_lol(names)
John
Eric
Cleese
Idle
Michael
Palin
>>> print_lol(names, True)
John
Eric
	Cleese
	Idle
Michael
	Palin
>>> print_lol(names, True, 4)
				John
				Eric
					Cleese
					Idle
				Michael
					Palin
>>> 
