#Zachary Frye
#CSC 500
#Module 3 Assignment
#Part 2

print('What is the current time? (in hours, use 0 to 23)') #prompts the user for the current time in hours
currentTime = int(input()) % 24 #get current time from user, mod 24 to prevent numbers outside of range
print('In how many hours will this alarm go off?') #prompts the user for number of hours until alarm goes off
hours = int(input()) #gets number of hours from input
print(f"The time when this alarm goes off will be: {(currentTime + hours) % 24}:00") #prints the calculation for the new time, uses fstring to remove the space after the variable calculation