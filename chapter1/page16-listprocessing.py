Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = ["The Holy Grail", 1975,
	  "The Life of Brain", 1979,
	  "The Meaning of Life", 1983]
>>> fav_movies = ["The Holy Grail", "The Life of Brain"]
>>> print(fav_movies[0])
The Holy Grail
>>> print(fav_movies[1])
The Life of Brain
>>> for each_flick in fav_movies:
	print(each_flick)

The Holy Grail
The Life of Brain
>>> count =0
>>> while count < len(movies):
	print(movies[count])
	count = count+1

The Holy Grail
1975
The Life of Brain
1979
The Meaning of Life
1983
>>> for each_item in movies:
	print(each_item)

The Holy Grail
1975
The Life of Brain
1979
The Meaning of Life
1983
>>> 
