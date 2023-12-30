# Python Functions
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
def my_function():
  print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
def my_function():
  print("Hello from a function")

my_function()

# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arguments are often shortened to args in Python documentations.
# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# ----------------------------------------------------------------
# Example
# ----------------------------------------------------------------
# This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
