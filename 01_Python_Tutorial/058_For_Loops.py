# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Example
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)