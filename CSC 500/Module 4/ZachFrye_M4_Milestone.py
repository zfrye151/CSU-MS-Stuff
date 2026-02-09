#Zachary Frye
#CSC 500
#M4 Milestone


class ItemToPurchase(): #create class for item to purchase
    item_name = "none" #defaults
    item_price = 0.00
    item_quantity = 0
   
    def print_item_cost(self): #function to print item cost
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}") #uses .2f to round to 2 decimal places, calculates the cost

item1 = ItemToPurchase() #creates item objects
item2 = ItemToPurchase()
print("Item 1") #print item and prompt for name
print("Enter the item name:")
item1.item_name = input()
print("Enter the item price:")
item1.item_price = float(input()) #prompt for price
print("Enter the item quantity:")
item1.item_quantity = int(input()) #prompt for quantity
print("Item 2") #print item and prompt for name
print("Enter the item name:")
item2.item_name = input()
print("Enter the item price:")
item2.item_price = float(input()) #prompt for price
print("Enter the item quantity:")
item2.item_quantity = int(input()) #prompt for quantity

print("TOTAL COST")
item1.print_item_cost() #run function to print cost
item2.print_item_cost()
total_cost = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price) #calculate total cost
print(f"Total: ${total_cost:.2f}") #print total cost