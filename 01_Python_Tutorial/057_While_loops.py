# Python Loops
# Python has two primitive loop commands:

# while loops
# for loops
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
# --------------------------------------------------------------------
# Example
# --------------------------------------------------------------------
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

# Note: remember to increment i, or else the loop will continue forever.

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# --------------------------------------------------------------------
# Example
# --------------------------------------------------------------------
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1