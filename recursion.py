# recursion:
# when a function calls itself again and again ,
# that function is called recursive function
# and the process is called recursion

# stack building
# def f1(x):
#     # base case
#     if x>5:
#         return
#     print(x)
#     f1(x+1)


# f1(1)


# stack falling
# def f1(x):
#     # base case
#     if x>5:
#         return
    
#     f1(x+1)

#     print(x)


# f1(1)


#WAP to find the power of number
# def power(a,b):
#     if b==0:
#         return 1
#     if b==1:
#         return a
#     return a*power(a,b-1)


# res = power(2,3)
# print(res)
#WAP to find the factorial of a number
# def f1(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return x*f1(x-1)

# res = f1(5)
# print(res)


#Write a program to find the sum of digits of number
# def f1(x):
#     if x==0:
#         return 0
#     else:
#         return x+f1(x-1)
# res=f1(5)
# print(res)             
#WAP to find the length of string
# def f1(x):
#     if x==0:
#         return 0
#     else:
#         return len(x)
# res=f1("helo")
# print(res)
#reverse of string using recursion
# def f1(x):
#     if len(x)==0:
#         return
#     print(x[-1],end="")
#     f1(x[:-1])

# f1("1291")



