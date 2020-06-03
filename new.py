##Name : Sumudu Herath
#Date: 26th Feb 2020
#Description : Tutorial 03

#Question 01
#part a

n = int(input("Give me a number over 100:"))
try:
    x=int(n)
    if x<=100:
        print(n,'is not over 100')

except ValueError:
    print("Please enter an valid integer")

#part b
n=input("Please enter your age")
try:
    x=int(n)
    if n>=18:
        print("Five can vote")
except ValueError:
    print("Please enter an valid integer,")