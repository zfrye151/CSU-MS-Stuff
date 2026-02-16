#Zach Frye
#CSC 500
#Module 5 Assignment part 2
#2/15/2026

print("How many books have you purchased this month?") #prompt user for number of books purchased
books = int(input())
if books < 0: #check if number of books is negative, if so prompt user to enter a non-negative integer
    print("Please enter a non-negative integer for the number of books.")
    books = int(input())

if books == 0 or books==1: #print points based on number of books purchased from 0 to 1, 2 to 3, 4 to 5, 6 to 7, and 8 or more
    print("You have earned 0 points.")
elif books == 2 or books == 3:
    print("You have earned 5 points!")
elif books == 4 or books == 5:
    print("You have earned 15 points!")
elif books == 6 or books == 7:
    print("You have earned 30 points!")
elif books >= 8:
    print("You have earned 60 points!")