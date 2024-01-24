#!/usr/bin/env python
# coding: utf-8

# # PHYS 105A:  Introduction to Scientific Computing
# 
# ## Unix shells, Remote Login, Version Control, etc
# 

# In order to follow this hands-on exercise, you will need to have the following software installed on your system:
# 
# * Terminal (built-in for windows, mac, and linux)
# * A Unix shell (Windows Subsystem for Linux; built-in for mac and linux)
# * Git
# * Jupyter Notebook or Jupyter Lab
# * Python 3.x
# 
# The easiest way to install these software is to use [Anaconda](https://www.anaconda.com/).

# ## Terminal and Unix Shell
# 
# This step is trivial if you are on Linux or on a Mac.  Simply open up your terminal and you will be given `bash` or `zsh`.
# 
# Or you have a laptop/computer running Linux.
# 
# If you are on Windows, you may start `cmd`, "Windows PowerShell", or the "Windows Subsystem for Linux".
# The former two don't give you a Unix shell, but you can still use it to navigate your file system, run `git`, etc.
# The last option is actually running a full Ubuntu environment that will give you `bash`.

# ## Once you are on a bash/zsh, try the following commands
# 
#     echo "Hello World" # the famous hello world program!
#     pwd # shows the current directory
#     ls # list all files
#     echo "Hello World" > hw.txt # stream text into a file
#     ls
#     cat hw.txt
#     mv hw.txt hello.txt
#     cp hello.txt world.txt
#     
# Awesome!  You are now a shell user!

# ## Git 
# 
# ### Pre-request
# 
# * Have a GitHub account
# * Have Jupyter Notebook/Lab set up on your machine
# * Have `git` (can be installed by conda)
# 
# ### Set up development environment
# 
# * `git config --global user.name "John Doe"`
# * `git config --global user.email johndoe@arizona.edu`
# 
# [Reference](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

# ## Create your own repository
# 
#     mkdir myrepo
#     cd myrepo
#     git init
#     touch test.txt
#     git add test.txt
#     git commit -m 'my first commit'
#     git remote add origin git@github.com:username/repository.git
#     git branch -M main
#     git push -u origin main
#     
# You probably need to add a SSH key to your GitHub account first.
# Follow instructions in your new repository

# ## Jupyter Notebook
# 
# A Jupyter Notebook is a JSON document containing multiple cells of text and codes.  These cells maybe:
# 
# * Markdown documentation
# * Codes in `python`, `R`, or even `bash`!
# * Output of the codes
# * RAW text

# ## Markdown Demo
# 
# This is a markdown demo.  Try edit this cell to see how things work.
# 
# See https://guides.github.com/features/mastering-markdown/ for more details.
# 
# 
# # This is an `<h1>` tag
# ## This is an `<h2>` tag
# ###### This is an `<h6>` tag
# 
# *This text will be italic*
# _This will also be italic_
# 
# **This text will be bold**
# __This will also be bold__
# 
# _You **can** combine them_
# 
# * Item 1
# * Item 2
#   * Item 2a
#   * Item 2b
#   
# 1. Item 1
# 1. Item 2
# 1. Item 3
#    1. Item 3a
#    1. Item 3b

# In[ ]:


## Python and Jupyter

# We can finally try jupyter and python as your calculator.
# Type some math formulas, then press Shift+Enter, jupyter will interpret your equations by python and print the output.

1 + 2 + 3 + 4


# In[2]:


# EXERCISE: Now, type your own equation here and see the outcome.
2 * 4



# In[3]:


10/5


# In[ ]:


# EXERCISE: Try to create more cells and type out more equations.

# Note that Jupyter supports "shortcuts"/"hotkeys".

# When you are typing in a cell, there is a green box surrounding the cell.
# You may click outside the cell or press "ESC" to escape from the editing mode.
# The green box will turn blue.

# You can then press "A" or "B" to create additional cells above or below the current active cell.


# In[4]:


50-18


# In[5]:


# One of the most powerful things programming languages are able to do is to assign names to values.
# This is in contrast to spreadsheet software where each "cell" is prenamed (e.g., A1, B6).
# A value associated with a name is called a variable.
# In python, we simply use the equal sign to assign a value to a variable.

a = 1
b = 1 + 1

# We can then reuse these variables.
a + b + 3


# In[6]:


# EXERCISE: create your own variables and check their values.
a = 7
b = 9
a * b -4


# In[7]:


# Sometime it is convenient to have mutiple output per cell.
# In such a case, you may use the python function `print()`
# Or the Jupyter function `display()`

print(1, 2)
print(a, b)

display(1, 2)
display(a, b)


# In[8]:


# EXERCISE: print and display results of equations
print(a * b)
display(17/3)


# In[ ]:


# Speaking of print(), in python, you may use both single or double quotes to create "string" of characters.

'This is a string of characters.'

"This is also a string of characters."

# You can mix strings, numbers, etc in a single print statement.
print("Num"+'bers:', 1, 2, 3)


# In[ ]:


# EXERCISE: assign a string to a variable and then print it



# In[ ]:


# In the lecture, we learned the different math operations in python: +, -, *, **, /, and //.
# Try to use them yourself.
# Pay special attention to the ** and // operators.

# * and ** are different
print(10*3)
print(10**3)

# / and // are different
print(10/3)
print(10//3)


# In[14]:


# EXERCISE: try out *, **, /, and // yourself.
# What if you use them for very big numbers?  Very small numbers?
# Do you see any limitation?
print(4 ** 8)
100 // a


# In[ ]:


# COOL TRICK: In python, you use underscores to help writing very big numbers.
# E.g., python knows that 1_000_000 is 1000_000 is 1000000.

print(1_000_000)
print(1000_000)
print(1000000)


# In[ ]:


# You can of course use scientific notation for numbers

c = 1.2e8
print(c)

# here c is a float number


# In[ ]:


# The integer division is logically equivalent to applying a floor function to the floating point division.
# However, the floor function is not a default (built-in) function.
# You need to import it from the math package:

from math import floor

print(10/3)
print(10//3)
print(floor(10/3))


# In[16]:


# EXERCISE: try to use the floor() function yourself

from math import floor

print(floor(17/5))


# In[ ]:


# There are many useful functions and constants in the math package.
# See https://docs.python.org/3/library/math.html

from math import pi, sin, cos

print(pi)
print(sin(pi))
print(cos(pi))


# In[19]:


# EXERCISE: what if you want to know cosine of 60 degree?

from math import cos,pi
print(cos(1 / 3 * pi))


# In[36]:


# assignment: test 5 additional functions from the math package below
# write one-line comment about what you are doing
# Python math package: https://docs.python.org/3/library/math.html

from math import floor, pi, sin, fabs, isnan, remainder, exp

#finding the absolute value of my function
x = 4
y = -10
print(abs(x * y))

#rounding the decimal of my output to a whole number
x = 17
y = 5
print(floor( x / y))

#finding the sin of 120 degrees
print(sin(2 / 3 * pi))

#finding the remainder of my division function (16 / 5)
print(remainder(16,y))

#finding e raised to the power of x
x = 5
print(exp(5))


# In[ ]:


# assignment: Create your repository in our organization
    
# repeat what we did from last class, but this time do it in our organization
# export this ipynb file into a python file, add it in the Git tree
# commit and push, you will use this when you collaborate for project


# In[ ]:


# compress this ipynb file and submit through D2L

