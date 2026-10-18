# n =int(input("Enter a number to find the factorial : "))
# fact = 1
# while n >= 1:
#     fact = fact * n
#     n-=1
# print(fact)


# find the sum of even number from 1 to 50
# n=1
# sum = 0
# while n<=50:
#     if n%2==0:
#         sum = sum + n
#     n+=1
# print(sum)

# find the sum of odd number from 1 to 50 number 
# n = 1
# sum = 0
# while n<=50:
#     if n%2!=0:
#         sum = sum + n
#     n+=1
# print(sum) 

# print the square of numbers from 1 to 10
# n =  1
# i = 0
# while n <= 10:
#     i =  n*n
#     n+=1
#     print(i) 

# print the  cube of 1 to 10 numbers
# n = 1 
# i = 0
# while n<=10:
#     i = n*n*n
#     n+=1
#     print(i)

# Count how many numbers are between 1 and 100 that are divisible by 5.
# n =  1
# count = 0
# while n<=100:
#     if n%5==0:
#         count+=1
#     n+=1
# print(count)

# Print the digits of a number one by one.
# n = 0
# while n <= 5:
#     n+=1
# print(n)

#Print the digits of a number one by one. 
# n = 1234
# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10 #remove the last digit from the number( // ) 
#Reverse a number using a while loop.
# n = 1234
# rev = 0
# while n>0:
#     digit = n%10
#     rev = rev*10+digit
#     n = n//10
# print(rev)

# list = [1,3,5,6,7,8]

# for items in list:
#     print(items)


# char = "shekhar"

# for str in char:
#     print(str)
# else:
#     print("END")

# char = "shekhar"

# for str in char:
#     if(str == 'e'):
#         print("e is found ")
#         break 
# print("end")

# print the elementsos the following list using a loop
# list =  [1,4,6,16,25,36,49,81,100]

# for num in list:
#  print(num)

# search for a number x in this tuple using a loop

# list = [1, 4, 6, 16, 25, 36, 49, 81, 100, 16]
# X = 16
# ind = 0
# for el in list:
#     if(X == el):
#         print("16 is found at index number : ",ind)
#     ind+=1
# print("END")


# range()
# for i in range(5): #here range(stop)
     
    # print(i,"hello")

# for i  in range(1,11): #Here Range(start,stop)
#     print(i)

# for i in range(2,12,2):
#     print(i)

# Even number using range() function
# for i in range (1,10,2):
#     print(i)


# print number from 1 to 100 
# for i in range(1,101):
#     print(i)

# print number from 100 to 1
# for i in range(100,0,-1):
#     print(i)

# multiplication table of 5 using range() function
# n = int(input("Enter the table number : "))
# for i in range(1,11):
#     print(n*i)

# n= int(input("Enter the number : "))

# for i in range(1,11):
#     print(n*i)

# pass stmt(null value)
# for i in range(5):
#     pass
# print("END")


# print the sum of n1 to n2 numbers

# n1 =  int(input("Enter n1 : "))
# n2 = int(input("Enter n2 : "))
# sum = 0
# while n1<=n2:
#     sum = sum+n1
#     n1+=1
# print("sum : ",sum)

# practice Questions :--------------------------------------------------------------------

# Print numbers from 1 to 10
# for i in range(1,11):
#     print(i)

# Print numbers from 10 to 1
# for i in range(10,0,-1):
#     print(i)
# ----------------------------------------------------------------------------------------------



# ----------------------------------------# Beginner #----------------------------------------#

# Print numbers from 1 to 10
# n = 1
# while n<=10:
#     print(n)
#     n+=1

# --------------------------------------------------
# Print numbers from 10 to 1.
# n = 10
# while n>=1:
#     print(n)
#     n-=1
# --------------------------------------------------
# Print all even numbers from 1 to 10
# n = 1
# while n<=10:
#     if(n%2==0):
#         print(n)
#     n+=1
# -------------------------------------------------
# Print all odd numbers from 1 to 20.
# n = 1
# while n<=20:
#     if(n%2!=0):
#         print(n)
#     n+=1
# ------------------------------------------------
# Print "Bappa" 5 times.
# n = 1
# while n<=5:
#     print(n,"Bappa")
#     n+=1
# ------------------------------------------------
# Print the multiplication table of a number entered by the user.
# n = 2
# i = 1
# while i<=10:
#     num = n*i
#     print(num)
#     i+=1
# -----------------------------------------------------
# Print numbers from 1 to N, where N is entered by the user.
# n = 1
# N = int(input("Enter the number : "))
# while n<=N:
#     print(n)
#     n+=1
# -----------------------------------------------------
# Find the sum of numbers from 1 to 10.
# i = 1
# n = 1
# sum = 0
# while n<=10:
#     sum = sum + n
#     n+=1 
# print("sum : ",sum)
# -----------------------------------------------------
# Find the sum of numbers from 1 to N
# i = 1
# sum = 0 
# n = int(input("Enter the number : "))
# while i<=n:
#     sum = sum + i
#     i+=1
# print(sum)
# -----------------------------------------------------
# Count from 1 to 100.
# n = 1
# while n<=100:
#     print(n)
#     n+=1

# --------------------------------# Easy #-------------------------------------------------------#
# Find the sum of even numbers from 1 to 50.
# n = 1
# sum = 0
# while n<=50:
#     if(n%2==0):
#         sum = sum + n
#     n+=1
# print("The sum of all even numbers between 1 to 50 is : ",sum)

# -------------------------------------------------------------------------------------
# Find the sum of odd numbers from 1 to 50.
# n = 1
# sum = 0
# while n<=50:
#     if(n%2!=0):
#         sum = sum + n
#     n+=1
# print("The sum of all the odd numbers bwtween 1 to 50 is  : ",sum)

# -------------------------------------------------------------------------------------
# Print the square of numbers from 1 to 10.
# n = 1
# while n <= 10:
#     sq = n * n
#     print(n," : ",sq)
#     n+=1
# -------------------------------------------------------------------------------------
# Print the cube of numbers from 1 to 10.
# n = 1
# sum = 0
# while n<=10:
#     cub = n * n * n
#     print(n,":",cub)
#     n+=1

# -------------------------------------------------------------------------------------
# Count how many numbers are between 1 and 100 that are divisible by 5.
# n = 1
# count = 0
# while n<=100:
#     if(n%5==0):
#         count+=1
#     n+=1
# print(count)
# -------------------------------------------------------------------------------------
# Find the factorial of a number.
# n = 5
# fact = 1
# while n>=1:
#     fact = fact*n
#     n-=1
# print(fact)
# -------------------------------------------------------------------------------------
# Print the digits of a number one by one.
# n = 1234
# while n>0:
#     digit = n%10
#     print(digit)
    # n=n//10    # // its call floor division it help us to remove the decimal part of the result.
# Count the number of digits in a number.
# n = 18
# num =0
# while n >0:
#         digit =  n%10
#         # print(digit)
#         num+=1
#         n = n//10
# print("total numbers : ",num)

# -------------------------------------------------------------------------------------
# Reverse a number using a while loop.
# n = 12345
# rev = 0 
# print("Original number is : ",n)
# while n>0:
#     digit = n%10
#     rev = rev *10 +digit
#     n = n//10
# print("After reversed number : ",rev) 

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# a = 1
# b = 2.65
# print(a+b)

# a = 23
# b = float(a)
# print(type(b))

# a = int(input("Enter the number : "))
# print("You entered ",a," number")
# print("their type is ",(type(a)))

# name = str(input("Enter your name : "))
# if name.isalpha():
#     print("Your name was registered as ",name)
# else:
#     print("Invalid name!")

# a = "shekhar"
# b = " shraddha"
# print(a + b)

# a = "shreyash"
# print(len(a))

# a = "shrivardhan"
# print(a[0:])

# a = "shrivardhan"
# print(a[-6:-3])

# a = "shekhar"
# print(a[::-1])

# a = "shekhar"
# print(a.endswith("ar"))
# print(a.capitalize())
# print(a.find("h"))
# print(a.count("h"))
# print(a.replace("shekhar","shraddha"))

# a = 82
# b = 83
# c = 87
# if a==b==c:
#     print("all values are equals")
# elif a >= b and a >= c:
#     print("Greatest number is:", a)
# elif b >= a and b >= c:
#     print("Greatest number is:", b)
# elif a==b==c:
#     print("all values are equals")
# else:
#     print("Greatest number is:", c)

# a=[34,76,45.2]
# print(len(a))

# a = [65,23,98,12,90,45,32]
# print(a[2:6])

# a = [34,65,23,22]
# a.append(43)
# print(a)
# a.sort()
# print(a)
# a.sort(reverse = True)
# print(a)
# a.reverse()
# print(a)
# a.insert(0,78)
# print(a)
# a.remove(22)
# print(a)
# a.pop(4)
# print(a)
