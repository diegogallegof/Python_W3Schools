# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#  ----------------------------------------------------------------
# Example
#  ----------------------------------------------------------------
# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# Sort Descending
# To sort descending, use the keyword argument reverse = True:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):
# ------------------------------------
# Example
# ------------------------------------
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)