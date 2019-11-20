Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'C:\\Users\\Aluminat\\AppData\\Local\\Programs\\Python\\Python38-32'
>>> os.chdir('D:\head-first\python\chapter3\HeadFirstPython\chapter3')
>>> os.getcwd()
'D:\\head-first\\python\\chapter3\\HeadFirstPython\\chapter3'
>>> 
>>> data = open('sketch.txt')
>>> print(data.readLine(), end='')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(data.readLine(), end='')
AttributeError: '_io.TextIOWrapper' object has no attribute 'readLine'
>>> print(data.readline(), end='')
Man: Is this the right room for an argument?
>>> print(data.readline(), end='')
Other Man: I've told you once.
>>> data.seek(0)
0
>>> data.tell()
0
>>> for each_line in data:
	print(each_line, end='')

Man: Is this the right room for an argument?
Other Man: I've told you once.
Man: No you haven't!
Other Man: Yes I have.
Man: When?
Other Man: Just now.
Man: No you didn't!
Other Man: Yes I did!
Man: You didn't!
Other Man: I'm telling you, I did!
Man: You did not!
Other Man: Oh I'm sorry, is this a five minute argument, or the full half hour?
Man: Ah! (taking out his wallet and paying) Just the five minutes.
Other Man: Just the five minutes. Thank you.
Other Man: Anyway, I did.
Man: You most certainly did not!
Other Man: Now let's get one thing quite clear: I most definitely told you!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh no you didn't!
Other Man: Oh yes I did!
Man: Oh look, this isn't an argument!
(pause)
Other Man: Yes it is!
Man: No it isn't!
(pause)
Man: It's just contradiction!
Other Man: No it isn't!
Man: It IS!
Other Man: It is NOT!
Man: You just contradicted me!
Other Man: No I didn't!
Man: You DID!
Other Man: No no no!
Man: You did just then!
Other Man: Nonsense!
Man: (exasperated) Oh, this is futile!!
(pause)
Other Man: No it isn't!
Man: Yes it is!
>>> data.close()
>>> 
