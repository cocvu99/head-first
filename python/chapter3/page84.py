Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> each_line = "I tell you, there's no such thing as a flying circus."
>>> each
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    each
NameError: name 'each' is not defined
>>> each_line.find(':')
-1
>>> each_line = "I tell you: there's no such thing as a flying circus."
>>> each_line.find(':')
10
>>> 
