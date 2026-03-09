#Zach Frye
#CSC 500
#Module 6 Portfolio Milestone
#3/8/2026

class ShoppingCart(): #create shopping cart class
    customer_name = "none" #defaults
    current_date = "January 1, 2020"
    cart_items = []

    def add_item(self, ItemToPurchase): #add item method
        print("ADD ITEM TO CART") #print add item to cart prompt
        print("Enter the item name:") #prompt for item name
        ItemToPurchase.item_name = input()
        print("Enter the item description:") #prompt for item description
        ItemToPurchase.item_description = input()
        print("Enter the item price:") #prompt for item price
        ItemToPurchase.item_price = float(input())
        print("Enter the item quantity:") #prompt for item quantity
        ItemToPurchase.item_quantity = int(input())
        self.cart_items.append(ItemToPurchase) #adds item to cart_items list

    def remove_item(self, item_name): #remove item method
        for item in self.cart_items: #iterates through cart_items list
            if item.item_name == item_name: #checks if item name matches item name to remove
                self.cart_items.remove(item) #removes item from cart_items list
                return
        print("Item not found in cart. Nothing removed.") #if item name not found, print error message

    def modify_item(self, ItemToPurchase): #modify item method
        for item in self.cart_items: #iterates through cart_items list
            if item.item_name == item_name: #checks if item name matches item name to modify
                print("Enter the new quantity:") #prompt for new quantity
                item.item_quantity = int(input()) #updates item quantity
                return
        print("Item not found in cart. Nothing modified.") #if item name not found, print error message

    def get_num_items_in_cart(self): #get number of items in cart method
        return len(self.cart_items) #returns the length of the cart_items list, which is the number of items in the cart

    def get_cost_of_cart(self):     #get cost of cart method, calculates total cost of items in cart
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):   #print total method, prints the total cost of items in cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self): #print descriptions method, prints the descriptions of items in cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

class ItemToPurchase(): #create class for item to purchase
    item_name = "none" #defaults
    item_price = 0.00
    item_quantity = 0
    item_description = "none"
   
    def print_item_cost(self): #function to print item cost
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}") #uses .2f to round to 2 decimal places, calculates the cost
    def print_item_description(self): #function to print item description
        print(f"{self.item_name}: {self.item_description}")

def print_menu(ShoppingCart): #function to print menu options
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("\nChoose an option:")

new_cart = ShoppingCart() #create new shopping cart object
print("Enter customer's name:") #prompt for customer name
new_cart.customer_name = input()
print("Enter today's date:") #prompt for current date
new_cart.current_date = input() 
print("\nCustomer name:", new_cart.customer_name) #print customer name and current date
print("Today's date:", new_cart.current_date)

while True:  # Add a loop here to keep returning to the menu
    print_menu(new_cart) #print menu and prompt for option
    choice = input() #get user input for menu option

    if choice == 'q': #check if user wants to quit, if so, quit program
        quit()
    elif choice == 'a': #check if user wants to add item to cart, if so, prompt for item attributes and add to cart
        new_item = ItemToPurchase() #create new item to purchase object
        new_cart.add_item(new_item) #call add item method to add item to cart

    elif choice == 'r': #check if user wants to remove item from cart, if so, prompt for item name and remove from cart
        print("REMOVE ITEM FROM CART") #print remove item from cart prompt
        print("Enter name of item to remove:") #prompt for item name to remove
        item_name = input()
        new_cart.remove_item(item_name)
        
    elif choice == 'c': #check if user wants to change item quantity, if so, prompt for item name and new quantity and update cart
        print("CHANGE ITEM QUANTITY") #print change item quantity prompt
        print("Enter the item name:") #prompt for item name to modify
        item_name = input()
        new_cart.modify_item(item_name)

    elif choice == 'i': #check if user wants to output items' descriptions, if so, print descriptions of items in cart and reprint menu options later
        print("OUTPUT ITEMS' DESCRIPTIONS")
        new_cart.print_descriptions()
        print("\n") #reprint menu options
    elif choice == 'o': #check if user wants to output shopping cart, if so, print total cost of items in cart and reprint menu options later
        print("OUTPUT SHOPPING CART")
        new_cart.print_total()
        print("\n")
    else: #check for invalid option, if so, print error message and reprint menu options until valid option is chosen
        print("Invalid option, please choose again.")
        # The loop will continue and prompt for input again