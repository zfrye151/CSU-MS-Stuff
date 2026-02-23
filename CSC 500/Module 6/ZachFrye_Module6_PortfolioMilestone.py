#Zach Frye
#CSC 500
#Module 6 Portfolio Milestone
#2/22/2026

class ShoppingCart(): #create shopping cart class
    customer_name = "none" #defaults
    current_date = "January 1, 2020"
    cart_items = []

    def add_item(self, ItemToPurchase): #add item method
        return
    def remove_item(self, item_name): #remove item method
        return
    def modify_item(self, ItemToPurchase): #modify item method
        return

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


print_menu(ShoppingCart) #print menu and prompt for option
example_cart = ShoppingCart() #example shopping cart object for now
example_cart.customer_name = "John Doe" #set name and date for example cart
example_cart.current_date = "February 22, 2026"
nike_r = ItemToPurchase() #example item objects for now, will be added to cart later
nike_r.item_name = "Nike Romaleos" #example item attributes, will be prompted for later
nike_r.item_price = 189.00
nike_r.item_quantity = 2
nike_r.item_description = "Volt color, weightlifting shoes"
choc_chips = ItemToPurchase() #example item objects for now, will be added to cart later
choc_chips.item_name = "Chocolate Chips" #example item attributes, will be prompted for later
choc_chips.item_price = 3.00
choc_chips.item_quantity = 5
choc_chips.item_description = "Semi-sweet"
powerbeats = ItemToPurchase() #example item objects for now, will be added to cart later
powerbeats.item_name = "Powerbeats 2 Headphones" #example item attributes, will be prompted for later
powerbeats.item_price = 128.00
powerbeats.item_quantity = 1
powerbeats.item_description = "Bluetooth headphones"
example_cart.cart_items = [nike_r, choc_chips, powerbeats] #add example items to example cart, will be added through menu options later

choice = input() #get user choice for menu option

if choice == 'q': #check if user wants to quit, if so, quit program
    quit()
elif choice == 'a': #check if user wants to add item to cart, if so, prompt for item attributes and add to cart
    print("ADD ITEM TO CART")
elif choice == 'r': #check if user wants to remove item from cart, if so, prompt for item name and remove from cart
    print("REMOVE ITEM FROM CART")
elif choice == 'c': #check if user wants to change item quantity, if so, prompt for item name and new quantity and update cart
    print("CHANGE ITEM QUANTITY")
elif choice == 'i': #check if user wants to output items' descriptions, if so, print descriptions of items in cart and reprint menu options later
    example_cart.print_descriptions()
    print("\n")
elif choice == 'o': #check if user wants to output shopping cart, if so, print total cost of items in cart and reprint menu options later
    example_cart.print_total()
    print("\n")
else: #check for invalid option, if so, print error message and reprint menu options until valid option is chosen
    print("Invalid option, please choose again.")
    choice = input()