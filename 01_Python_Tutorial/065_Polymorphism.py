# Python Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to 
# methods/functions/operators with the same name that can be executed on many objects or classes.

# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# String
# For strings len() returns the number of characters:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
x = "Hello World!"

print(len(x))

# Tuple
# For tuples len() returns the number of items in the tuple:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

#  Dictionary
# For dictionaries len() returns the number of key/value pairs in the dictionary:

# Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))