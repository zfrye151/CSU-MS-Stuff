#Zach Frye
#CSC 500
#Module 5 Assignment part 1
#2/15/2026


print("How many years of rainfall should this program calculate?") #prompt user for number of years to calculate
year = int(input())
if year < 1: #check if year is negative, if so prompt user to enter a positive integer
    print("Please enter a positive integer for the number of years.")
    year = int(input())
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #array for months of the year
total_rainfall = 0.0 #declare total rainfall variable

for i in range(year): #for loop for year increment
    for month in months: #for loop for month increment
        print("How many inches of rainfall were there in " + month + " of year " + str(i+1) + "?") #prompt user for rainfall in each month of each year
        rainfall = float(input()) #set rainfall variable
        if rainfall >= 0: #check if rainfall is negative, if not add to total rainfall, if so prompt user to enter a non-negative number
            total_rainfall += rainfall
        else:
            print("Please enter a non-negative number for rainfall.")
            rainfall = float(input())

print("Total number of months:", year*12) #calculate and print total number of months, total rainfall, and average rainfall per month
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {total_rainfall/(year*12):.2f} inches")