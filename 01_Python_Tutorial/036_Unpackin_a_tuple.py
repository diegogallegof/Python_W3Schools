# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Packing a tuple:

fruits = ("apple", "banana", "cherry")
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)