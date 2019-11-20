Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nester
>>> cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
>>> print_lol(cast)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print_lol(cast)
NameError: name 'print_lol' is not defined
>>> nester.print_lol(cast)
Palin
Cleese
Idle
Jones
Gilliam
Chapman
>>> 
