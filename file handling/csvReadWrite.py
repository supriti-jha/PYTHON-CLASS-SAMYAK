# data = [{"id":101,"name":"ravi","marks":99},
#         {"id":102,"name":"amit","marks":49},
#         {"id":103,"name":"shyam","marks":19},
#         {"id":104,"name":"ravi kishan","marks":82},
#         {"id":105,"name":"ram","marks":90}]


# import csv
# # #comma separated values - excel file
# with open("abc.csv","w") as file:
#     writer = csv.DictWriter(file,fieldnames=["id","name","marks"])
#     writer.writeheader()
#     writer.writerows(data)


# with open("abc.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# student = [{"roll no":1,"name":" ram","marks":99},
#            {"roll no":2,"name":" mohan","marks":98},
#            {"roll no":3,"name":" shyam","marks":97},
#            {"roll no":4,"name":" krishna","marks":96}]
# import csv
# with open("abc.csv","w") as file:
#     writer = csv.DictWriter(file,fieldnames=["roll no","name","marks"])
#     writer.writeheader()
#     writer.writerows(student)
# with open("abc.csv","r") as file:
#     reader =csv.DictReader(file)
#     for row in reader:
#         print(row)    

# info =[{"roll no":-=1,"name":"abc","age":12},
#        {"roll no":2,"name":"efg","age":13},
#        {"roll no":3,"name":"hij","age":14},
#        {"roll no":4,"name":"klm","age":15}]
# import csv
# with open("abc.csv","w") as file:
#     writer = csv.DictWriter(file,fieldnames=["roll no","name","age"])
#     writer.writeheader()
#     writer.writerows(info)
# 
# with open("info.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print (row)

# Write a Python program to read each row from a given csv file and print a list of strings.
# import csv
# with open("abc.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print (row)

# Write a Python program to read a given CSV file as a list.
# infor=[{1,2,3,4,5,6,7}]
# import csv
# with open("infor.csv","w") as file:
#      writer = csv.DictWriter(file,fieldnames=[])
#      writer.writeheader()
#      writer.writerows(infor)     
# with open("infor.csv","r") as file:
#      reader=csv.DictReader(file)
#      for row in reader:
#          print (row)
# Write a Python program to read a given CSV file as a list.
# import csv

# lstr = ["supriti", "tinki", "jha"]

# with open("abc.csv", "r") as file:
#     reader = csv.reader(file)   # Correct: 'reader', not 'Reader'
    
#     dataread = []
#     for row in reader:
#         dataread.append(row)

# print(dataread)


# Write a Python program to read a given CSV file as a dictionary. Scripting Languages
# info =[{"roll no":1,"name":" abc","age":12},
#         {"roll no":2,"name":"efg","age":13},
#         {"roll no":3,"name":"hij","age":14},
#         {"roll no":4,"name":"klm","age":15}]
# import csv
# with open("info.csv","w") as file:
#      writer = csv.DictWriter(file,fieldnames=["roll no","name","age"])
#      writer.writeheader()
#      writer.writerows(info)

# with open("info.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print (row)

# Write a function that takes a filename as input and returns the total number of characters in that file 
# (including spaces and newlines).

files=input("enter file name :")
with open(files,"r") as file:
      ans=file.read()
      data=len(ans)
print(data)
