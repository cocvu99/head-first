Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from distutils.core import setup
setup(
	name 		= 'nester',
	version 	='1.0.0',
	py_modules 	=['nester'],
	author 		='hfpython',
	author_email 	= 'hfpython@headfirstlabs.com',
	url 		= 'https://headfirstlabs.com',
	description 	= 'A simple printer of nested lists',
	)
