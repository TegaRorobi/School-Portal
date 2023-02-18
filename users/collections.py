# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# ============COUNTER -> <class 'collections.Counter'> ============== #
from collections import Counter
'''
__dir__() method of a counter without the magic methods i.e([mtd for mtd in dir(myCounter) if '__' not in mtd]):
[
'_keep_positive', 'clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 
'pop', 'popitem', 'setdefault', 'subtract', 'total', 'update', 'values'
]
''' 

myString = 'aaabbbbcccccd'
# Counter class produces a dictionary containing the unique individual  items of the string as the keys and the number of 
# occurences of the string as the value
myCounter = Counter(myString) #Counter({'c': 5, 'b': 4, 'a': 3, 'd': 1})
# print(myCounter)

# this returns a list of tuples. the number of tuples is determined by the argument of the most_common method.
# myCounter.most_common(1) gives out a list of one tuple with the first value as the key and the second value as 
# the number of occurrences of the key in the counter. if the argument was 2, then it will give a list 2 tuples
# of the first two most occuring elements in the counter.
# print(myCounter.most_common(2))

# print(myCounter.elements()) #creates an iterable from the counter with each key present as many times as its value in the counter









# ================= NAMEDTUPLE <class '__main__.myNamedTuple'>=========================#
from collections import namedtuple
# dir method of a namedtuple ( without the magic methods )
# ['_fields', '_field_defaults', '_make', '_replace', '_asdict', 'x', 'y', 'index', 'count']

# a namedtuple kind of creates a class with the name of the class as the first argument and the arguments of the 
# class as the second argument

# the __dir__() method of the following class is just ['x', 'y']
class myClass:
	def __init__(self, x, y):
		self.x, self.y = x, y
	def __repr__(self):
		return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

# this one line of code creates a class and with attributes of the values in the second argument of the string
# it is similar to the class I created above, but it has more methods and attributes than the class I created above
myNamedTuple = namedtuple('myNamedTuple', 'x, y')

pt = myClass(-1, 4)
pt2 = myNamedTuple(7, -3)

# print(pt.x)
# print(pt2)

# import sys
# import re
# regex = r'(?P<preceeding_backslash>\\)(?P<file_name>\w+)(?P<filename_extension>\.[a-zA-Z]{2,})'
# regex = '(?P<preceeding_backslash>\\\\)(?P<file_name>\w+)(?P<filename_extension>\.[a-zA-Z]{2,})'
# file_name = re.search(regex, sys.argv[0]).group('file_name')
# print(file_name)











# ================= ORDEREDDICT <class 'collections.OrderedDict'> =================#
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'move_to_end', 
# 'pop', 'popitem', 'setdefault', 'update', 'values']
from collections import OrderedDict

# orderedDicts are pretty much legacy since python 3.7+ as normal dictionaries remember their order also
my_ordered_dict = OrderedDict()
my_ordered_dict['a'] = 1
my_ordered_dict['b'] = 2
my_ordered_dict['c'] = 3
my_ordered_dict['d'] = 4

# this comes out tuples of keys, values
# print(my_ordered_dict)










#================== DEFAULTDICT <class 'collections.defaultdict'> ==================#
# ['clear', 'copy', 'default_factory', 'fromkeys', 'get', 'items', 'keys', 
# 'pop', 'popitem', 'setdefault', 'update', 'values']

from collections import defaultdict

# this creates a dictionary with a default class bool and in the case that there is a search for a key that does 
# not exist in the dictionary, the default value for the class is the output.
myDefaultDict  = defaultdict(bool)
myDefaultDict['a'] = 1
myDefaultDict['b'] = 2
# print(myDefaultDict['a'])
# print(myDefaultDict['z']) # output is the default value for a bool type i.e False





# ===============DEQUE <class 'collections.deque'> =================#

# a deque is a double-ended queue and it can be used to add or remove elements from both ends

['append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index', 'insert', 
'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate']
from collections import deque
myDeque = deque()

myDeque.append(1)
myDeque.append(2)
myDeque.append(3)

myDeque.appendleft(4)
myDeque.appendleft(5)

myDeque.popleft()
myList = list(range(7, 10))

myDeque.extendleft(myList)

print(myDeque, 'not rotated')

myDeque.rotate(-3)
print(myDeque, 'rotated')