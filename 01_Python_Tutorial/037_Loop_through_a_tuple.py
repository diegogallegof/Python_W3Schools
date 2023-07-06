# You can loop through the tuple items by using a for loop.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Learn more about for loops in our Python For Loops Chapter.

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop
# You can loop through the tuple items by using a while loop.

# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1