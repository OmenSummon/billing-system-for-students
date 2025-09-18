class BurgerBillingSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "Aloo Tikki", "price": 5},
            2: {"name": "Maharaja", "price": 10},
            3: {"name": "Mac Special", "price": 15},
            4: {"name": "Cheese Burger", "price": 8},
            5: {"name": "Chicken Deluxe", "price": 12},
            6: {"name": "Veg Supreme", "price": 9}
        }
        self.orders = []
        
    def display_menu(self):
        print("\n" + "="*50)
        print("         🍔 WELCOME TO BURGER PALACE 🍔")
        print("="*50)
        print("Sr.  Name               Price")
        print("-" * 35)
        for sr, item in self.menu.items():
            print(f"{sr:<4} {item['name']:<18} ${item['price']}")
        print("="*50)
    
    def get_order(self):
        while True:
            try:
                choice = int(input("\nEnter your choice (1-6): "))
                if choice in self.menu:
                    return choice
                else:
                    print("Invalid choice! Please select from 1-6.")
            except ValueError:
                print("Please enter a valid number!")
    
    def get_quantity(self):
        while True:
            try:
                quantity = int(input("How many quantity? "))
                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0!")
            except ValueError:
                print("Please enter a valid number!")
    
    def check_student_discount(self):
        while True:
            student = input("Are you a student? (yes/no): ").lower().strip()
            if student in ['yes', 'y']:
                return True
            elif student in ['no', 'n']:
                return False
            else:
                print("Please enter 'yes' or 'no'")
    
    def check_delivery(self):
        while True:
            delivery = input("Do you want delivery? (yes/no): ").lower().strip()
            if delivery in ['yes', 'y']:
                return True
            elif delivery in ['no', 'n']:
                return False
            else:
                print("Please enter 'yes' or 'no'")
    
    def get_tip(self):
        while True:
            tip_choice = input("Do you want to give tip? (yes/no): ").lower().strip()
            if tip_choice in ['no', 'n']:
                return 0
            elif tip_choice in ['yes', 'y']:
                print("Tip options: $2, $5, $10")
                while True:
                    try:
                        tip = int(input("Enter tip amount (2/5/10): $"))
                        if tip in [2, 5, 10]:
                            return tip
                        else:
                            print("Please choose from $2, $5, or $10")
                    except ValueError:
                        print("Please enter a valid number!")
            else:
                print("Please enter 'yes' or 'no'")
    
    def add_single_order(self):
        choice = self.get_order()
        item = self.menu[choice]
        quantity = self.get_quantity()
        
        order = {
            'sr': choice,
            'name': item['name'],
            'price': item['price'],
            'quantity': quantity,
            'total_price': item['price'] * quantity
        }
        
        self.orders.append(order)
        print(f"\n✅ Added {quantity} x {item['name']} to your order!")
    
    def continue_ordering(self):
        while True:
            continue_order = input("\nDo you want to add more items? (yes/no): ").lower().strip()
            if continue_order in ['yes', 'y']:
                return True
            elif continue_order in ['no', 'n']:
                return False
            else:
                print("Please enter 'yes' or 'no'")
    
    def calculate_bill(self):
        if not self.orders:
            print("No orders placed!")
            return
        
        # Get billing preferences
        is_student = self.check_student_discount()
        wants_delivery = self.check_delivery()
        tip_amount = self.get_tip()
        
        # Calculate subtotal
        subtotal = sum(order['total_price'] for order in self.orders)
        
        # Calculate discounts and charges
        student_discount = subtotal * 0.20 if is_student else 0
        delivery_charge = subtotal * 0.05 if wants_delivery else 0
        
        # Calculate final total
        final_total = subtotal - student_discount + delivery_charge + tip_amount
        
        # Print the bill
        self.print_bill(subtotal, student_discount, delivery_charge, tip_amount, final_total)
    
    def print_bill(self, subtotal, student_discount, delivery_charge, tip_amount, final_total):
        print("\n" + "*" * 60)
        print("                    FINAL BILL")
        print("*" * 60)
        print("Sr.  Name               Price  Quantity  Total Price")
        print("-" * 55)
        
        for order in self.orders:
            print(f"{order['sr']:<4} {order['name']:<18} ${order['price']:<6} {order['quantity']:<8} ${order['total_price']}")
        
        print("-" * 55)
        print(f"                                    Subtotal: ${subtotal:.2f}")
        
        if student_discount > 0:
            print(f"Student Discount (20%)                      -${student_discount:.2f}")
        
        if delivery_charge > 0:
            print(f"Delivery Charge (5%)                        +${delivery_charge:.2f}")
        
        if tip_amount > 0:
            print(f"Tip                                         +${tip_amount:.2f}")
        
        print("-" * 55)
        print(f"TOTAL BILL                                  ${final_total:.2f}")
        print("*" * 60)
        print("\n        🎉 THANK YOU AND COME AGAIN! 🎉")
        print("          Have a great day ahead! 😊")
        print("*" * 60)
    
    def run(self):
        print("🍔 Starting Burger Billing System...")
        
        while True:
            self.display_menu()
            
            # Take orders
            while True:
                self.add_single_order()
                if not self.continue_ordering():
                    break
            
            # Calculate and display bill
            self.calculate_bill()
            
            # Ask if customer wants to place another order
            while True:
                new_order = input("\nWould you like to place a new order? (yes/no): ").lower().strip()
                if new_order in ['yes', 'y']:
                    self.orders = []  # Clear previous orders
                    break
                elif new_order in ['no', 'n']:
                    print("\n🍔 Thank you for visiting Burger Palace! Goodbye! 👋")
                    return
                else:
                    print("Please enter 'yes' or 'no'")

# Main program
if __name__ == "__main__":
    billing_system = BurgerBillingSystem()
    billing_system.run()
