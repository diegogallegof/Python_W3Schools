# Removing Items
# There are several methods to remove items from a dictionary:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)