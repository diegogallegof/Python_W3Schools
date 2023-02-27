'''
Built-in Data Types

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
'''
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

'''
Getting the Data Type
You can get the data type of any object by using the type() function:
'''
#Example
#Print the data type of the variable x:

x = 5
print(type(x))

# Example	Data Type	Try it

#str
x = "Hello World"

#int			
x = 20	

#float
x = 20.5

#complex
x = 1j	

#list	
x = ["apple", "banana", "cherry"]	

#tuple	
x = ("apple", "banana", "cherry")	

#range	
x = range(6)	

#dict	
x = {"name" : "John", "age" : 36}	

#set
x = {"apple", "banana", "cherry"}		

#frozenset
x = frozenset({"apple", "banana", "cherry"})	
print(x)	

#bool
x = True	

#bytes	
x = b"Hello"	

#bytearray	

x = bytearray(5)	

#memoryview	
x = memoryview(bytes(5))	

#NoneType
x = None	