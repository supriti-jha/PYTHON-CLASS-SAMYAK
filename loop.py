# what is loop?
# DRY - Dont Repeat Yourself
#start,end,stepsize
#range->small to big->end->+1
#range->big to small->end->-1

# for i in range(1,11,2):
#     print(i)

#reverse counting
# for i in range(10,0,-1):
#     print(i)

#reverse range
# for i in reversed(range(1,11)):
#     print(i)

#control flow of Loop
#break,continue,pass
#break keyword is used to transfer the control flow outside the loop
# for i in range(1,1000000000000000000000000001):
#     if i==11:
#         break
#     print(i)

# for i in range(1,11):
#     pass#In future , some logic will come here

#continue
# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)


#Q1. print the table of 2 as shown below:
# 2X1=2
# 2X2=4
# .
# .
# 2X10=20
# for i in range (2,11):
#     x=(2*i)
#     print("2 X",i,"=",x)    

# Q2. Write a program to find the sum of first 10 natural numbers
# n=0
# for i in range (1,11):
#  n=n+i
#  print(i)
# print(n)

# 26th march
#Q3. write a program to find factorial of a number
# 5 - 1X2X3X4X5

x = int(input("Enter no:"))
fact = 1

for i in range(1,x+1):
    fact = fact*i

print(fact)

# Q4. write a program to print first 10 no's of fibonacci
# # series
# 0 1 1 2 3 5....
# f=0
# s=1
# # print(f)
# # print(s)

# for i in range(5):
#     t=f+s
#     print(t)

#Q5 Write a program to check whether a no is prime or not
# x  = int(input("Enter No:"))
# # 7- 2to6
# #10 - 2,3,4,5,6,,7,8,9
# for i in range(2,x):
#     if x%i==0:
#         print("Not Prime")
#         break
# else:
#     print("Prime No")

# Q6. Write a program to find sum of digits of number
# x = 12691
# # 1+2+6=9
# res=0
# for i in range(len(str(x))):
#     rem=x%10
#     res+=rem
#     x=x//10
# print(res)
# Q7. Write a program to find reverse of number

# x = 1765432456789
# # 1+2+6=9
# res=0
# for i in range(len(str(x))):
#     rem=x%10
#     res=res*10+rem
#     x=x//10
# print(res)

#27th March 2026
#pattern 
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)

# *****
# ****
# ***
# **
# *


# for i in reversed(range(1,6)):
#     print("*"*i)

#     *
#    **
#   ***
#  ****
# *****

# for i in range(1,6):
#     print(" "*(5-i)+"*"*i)


# Nested Loop:
# for i in range(1,4):
#     for j in range(i):
#         print(i,j)

#wap to print prime nio b/w 1to100

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
 
#wap to print pattern using nested loop
# *
# **
# ***
# ****
# *****

# for row in range(1,6):
#     for col in range(row):
#         print("*",end="")
#     print()#next line.

#write a program to print reverse pattern using nested loop.


# for row in reversed(range (1,6)):
#     for col in range(row):
#         print("*",end="")
#     print()


# for row in range (1,6):
#     print(" "*(5-row),end="")
#     for col in range(row):
#         print("* ",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j==1 or j==5 or i==3:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()            


# for i in range(1,6):
#      for j in range(1,6):
#         if j==1 or j==5 or i==j:
#              print("*",end="")
#         else:
#              print(" ",end="")
#      print()    
# WRITE A PROGRAM TO FIND SUM OF ALL ELEMENTS OF LIST
# a=[1,2,3,4,5,6,7,8,9,10]
# # print(sum(a))
# result=0
# for item in a:
#    result+=item
# print(result)   


# WRITE A PROGRAM TO REMOVE ODD NO FROM LIST
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2!=0:
#      a.remove(i)
# print(a)        

# # WRITE A PROGRAM TO FIND SUM OF ALL ELEMENTS OF LIST
# a=[1,9,10,27,98,96,77]
# larg=a[0]
# for item in a:
#    if item >larg:
#      larg=item
# print(larg)     
