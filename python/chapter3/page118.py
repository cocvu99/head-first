Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	data = open('missing.txt')
	print(data.readline(), end='')
except IOError:
	print('File error')
finally:
	data.close()

File error
Traceback (most recent call last):
  File "<pyshell#7>", line 7, in <module>
    data.close()
NameError: name 'data' is not defined
>>> 
