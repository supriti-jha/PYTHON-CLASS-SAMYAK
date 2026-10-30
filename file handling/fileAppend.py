data = '''hello
welcome to python programming
Lets Learn File Handling
'''


with open("abc.txt","a") as file:
    file.write(data)