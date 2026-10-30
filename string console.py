# Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
# Enter "help" below or click "Help" above for more information.
# #String-string is python's immutable(non changeable) data type
# #list
# >>> x=[1,2,3]
# >>> x[2]
# 3
# >>> x[2]=100
# >>> x
# [1, 2, 100]
# >>> #mutable
# >>> del x[2]
# >>> x
# [1, 2]
# >>> x = "hey welcome to samyak institute"
# >>> x[0]
# 'h'
# >>> x[0]="H"
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     x[0]="H"
# TypeError: 'str' object does not support item assignment
# >>> del x[0]
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     del x[0]
# TypeError: 'str' object doesn't support item deletion
# >>> x
# 'hey welcome to samyak institute'
# >>> x.replace("h","H")
# 'Hey welcome to samyak institute'
# x
# 'hey welcome to samyak institute'
# x = x.replace("h","H")
# x
# 'Hey welcome to samyak institute'
# x = 'hey'
# print(x)
# hey
# x = "hey"
# print(x)
# hey
# x = "hey "python""
# SyntaxError: invalid syntax
# x = 'hey "python"'
# print(x)
# hey "python"
# x = "hey \"python\""#escape sequence
# x
# 'hey "python"'

# #operators membership,identity,walrus operator
# x = "aeiuoAEIUO"
# char = "x"
# char in x
# False
# #DRY - dont repeat yourself
# char = "a"
# char in x
# True
# #identity operator
# #is,is not
# x = 5
# y = 5
# x is y
# True
# #walrus operator
# x
# 5
# x = 10
# print(x)
# 10

# print(x:=20)#:= is known as walrus operator
# 20
# x
# 20
# #multiline string
# x = "Primary Uses of Python:
# Data Science & Data Visualization: Handling, analyzing, and visualizing complex data sets.
# Artificial Intelligence & Machine Learning: Creating algorithms for AI-driven applications.
# Web Development (Back-end): Building server-side applications using frameworks like Django and Flask.
# Automation & Scripting: Writing code to automate repetitive tasks. 
# Amazon Web Services (AWS)
# Amazon Web Services (AWS)
#  +4"
 
# SyntaxError: unterminated string literal (detected at line 1)
# x = '''Primary Uses of Python:
# Data Science & Data Visualization: Handling, analyzing, and visualizing complex data sets.
# Artificial Intelligence & Machine Learning: Creating algorithms for AI-driven applications.
# Web Development (Back-end): Building server-side applications using frameworks like Django and Flask.
# Automation & Scripting: Writing code to automate repetitive tasks. 
# Amazon Web Services (AWS)
# Amazon Web Services (AWS)
#  +4'''
# x = """Primary Uses of Python:
# Data Science & Data Visualization: Handling, analyzing, and visualizing complex data sets.
# Artificial Intelligence & Machine Learning: Creating algorithms for AI-driven applications.
# Web Development (Back-end): Building server-side applications using frameworks like Django and Flask.
# Automation & Scripting: Writing code to automate repetitive tasks. 
# Amazon Web Services (AWS)
# Amazon Web Services (AWS)
#  +4"""
# x = "Hey Welcome to Python"
# x.upper()
# 'HEY WELCOME TO PYTHON'
# x.lower()
# 'hey welcome to python'
# x.capitalize()
# 'Hey welcome to python'
# x.title()
# 'Hey Welcome To Python'
# x
# 'Hey Welcome to Python'
# x.swapcase()
# 'hEY wELCOME TO pYTHON'
# x
# 'Hey Welcome to Python'
# x[-1]
# 'n'
# x[2]
# 'y'
# x[-2]
# 'o'
# x
# 'Hey Welcome to Python'
# #substring
# x[0:3]
# 'Hey'
# x[0:7]
# 'Hey Wel'
# x[0:]
# 'Hey Welcome to Python'
# x[:]
# 'Hey Welcome to Python'
# x[0:9:1]
# 'Hey Welco'
# x[0:9:2]
# 'HyWlo'
# x[::-1]
# 'nohtyP ot emocleW yeH'
# #reverse of string
# x
# 'Hey Welcome to Python'
# x.find("e")#first occurence
# 1
# x.rfind("e")#last occurence
# 10
# x.find("e",2)
# 5
# x.index("e",2)
# 5
# x.find("X")
# -1
# x.index("X")
# Traceback (most recent call last):
#   File "<pyshell#78>", line 1, in <module>
#     x.index("X")
# ValueError: substring not found
# x = "amit"
# len(x)
# 4
# x = 'Hey Welcome to Python'
# x.split()
# ['Hey', 'Welcome', 'to', 'Python']
# y = x.split()
# y
# ['Hey', 'Welcome', 'to', 'Python']
# len(y)
# 4
# type(y)
# <class 'list'>
# x
# 'Hey Welcome to Python'
# type(x)
# <class 'str'>
# y
# ['Hey', 'Welcome', 'to', 'Python']
# #list to string

# " ".join(y)
# 'Hey Welcome to Python'
# "#".join(y)
# 'Hey#Welcome#to#Pythonx=
# x='aeiouAEIOU'
# char="a"
# char in x
