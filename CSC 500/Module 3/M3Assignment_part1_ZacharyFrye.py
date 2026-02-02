#Zachary Frye
#CSC 500
#Module 3 Assignment
#Part 1

print('Please enter the subtotal for the order:') #prompts the user for the subtotal
subtotal = round(float(input()),2) #gets input from the user and rounds to two decimal places
tip = round((subtotal * 0.18),2) #calculates the tip amount and rounds to two decimal places
tax = round((subtotal*0.07),2) #calculates the sales tax amount and rounds to two decimal places
total = round((subtotal + tip  + tax),2) #calculates the overall total by adding the three variables together, rounds to 2 decimal places
print('The tip amount is: $', tip) #prints the tip amount
print('The sales tax is: $', tax) #prints the sales tax amount
print('The overall total for this order is: $', total) #prints the overall total of the meal