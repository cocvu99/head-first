Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
>>> movies.insert(1, 1975)
>>> movies.insert(3, 1979)
>>> movies.insert(5, 1983)
>>> print(movies)
['The Holy Grail', 1975, 'The Life of Brain', 1979, 'The Meaning of Life', 1983]
>>> movies.pop()
1983
>>> movies = ["The Holy Grail", 1975, "The Life of Brain", 1979, "The Meaning of Life", 1983]
>>> movies.pop()
1983
>>> movies.append(1983)
>>> print(movies)
['The Holy Grail', 1975, 'The Life of Brain', 1979, 'The Meaning of Life', 1983]
>>> 
