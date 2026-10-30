data = '''hello
welcome to python programming
Lets Learn File Handling
'''
# w - write
# file = open("abc.txt","w")
# file.write(data)
# file.close()

with open("abc.txt","w") as file:
    file.write(data)