# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
# ----------------------------------------------------------------
#   Example
# ----------------------------------------------------------------
# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)