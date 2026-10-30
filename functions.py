# USER DEFINED FUNCTION
#function definition
#default function
# def f1():
#     print("Function Called...")
#function calling
# f1()

# parameterised function
# def f1(x,y):
    # return x+y

# function calling
# res=f1(12,13)
# print(res)
#Return statement vs Yield Statement
# def f1():
#     for i in range(1,101):
#         return i
# function k bahar value return krdo jaha se function call hua
# res = f1()
# print(res)

# def f1():
#     for i in range(1,11):
#         yield i

# res = f1()
# print(res)

#wap to create a calculator using function
# x=int(input("enter no1."))
# y=int(input("enter no2."))
# choice=input("Enter +-/* : ")

# def f1(x,y):
#     return (x+y)
# def f2(x,y):
#     return (x-y)
# def f3(x,y):
#     return (x*y)
# def f4(x,y):
#     return (x/y)

# if choice=="+":
#     ans=f1(x,y)
# elif choice=="-":
#     ans=f2(x,y)
# elif choice=="*":
#     ans=f3(x,y)
# elif choice=="x":
#     ans=f4(x,y)
# else :
#     ans="error"

# print(ans)

# x=int(input("enter no1."))
# y=int(input("enter no2."))
# choice=input("Enter +-/* : ")

# def f1(x,y):
#     return (x+y)
# def f2(x,y):
#     return (x-y)
# def f3(x,y):
#     return (x*y)
# def f4(x,y):
#     return (x/y)

# d = {"+":f1,"-":f2,"*":f3,"/":f4}
# res = d[choice](x,y) if choice in "+-/*" else "Invalid Choice"
# print(res)


# x=input("enter no1.")
# y=input("enter no2.")
# choice=input("Enter +-/* : ")

# def f1(x,y,choice):
#     print(eval(x+choice+y))

# f1(x,y,choice)
# 9Apr2026
#types of parameters
# optional parameter
# def f1(x,y=0):
#     print(x,y)

# f1(1,4)
#args and kwargs(keyworded arguments)
# def student(name,cls,*extra):
#     print(name,cls,extra)

# def student(name,cls,**extra):
#     print(name,cls,extra)

# student("Ravi",10,father="Amit",gender="Male",contact="9876543210")
# student("Ravi",10,"Male","Amit",9876543210)
#lambda function & some important functions
# single line function
# def Sum(x,y):
#     return x+y
# print(Sum(1,2))

# sum = lambda x,y : x+y
# print(sum(1,5))

# x = [1,2,3,4,5,6,7,8,9,10]

# square = lambda a:a**2
#map method
# result=list(map(square,x))
# print(result)

# filter method
# x = [1,2,3,4,5,6,7,8,9,10]
# # def EvenOdd(a):
# #     if a%2==0:
# #         return "Even"
# #     else:
# #         return "Odd"
    
# evenOdd = lambda a: True if a%2!=0 else False
# res = list(filter(evenOdd,x))
# print(res)
#single line function

#Recursive Function
# if no is positive or  not 
# a=[1,4,-4,-45,-6,-8]
# positive= lambda a:True if a<0 else False
# res=list(filter(positive,a))
# print(res)

