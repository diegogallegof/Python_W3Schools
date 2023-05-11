# Loop Through a List
# You can loop through the list items by using a for loop:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#   Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])