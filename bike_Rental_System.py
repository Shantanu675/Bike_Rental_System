import tkinter as tk
from tkinter import messagebox

class BikeShowroom:
    def __init__(self, bikes_available=120):
        self.bikes_available = bikes_available
        self.bikes_name_and_number = {
            "Royal Enfield": 10, "Honda SP 125": 20, "Hero Splendor Plus": 25,
            "Honda": 25, "TVS Raider": 10, "Yamaha": 15, "Kawasaki": 5, "Ducati": 10
        }
        self.bikes_rent = {"Daily": 100, "Weekly": 600, "Monthly": 2500}

    def display_available_bikes(self):
        bikes_text = "Name of Bikes : Quantity of Bikes\n"
        for Name, Quantity in self.bikes_name_and_number.items():
            bikes_text += f"{Name.capitalize()}  :  {Quantity}\n"

        bikes_text += "\nTotal Numbers of Bikes Available : {}\n\n".format(
            self.bikes_available)

        return bikes_text

    def display_rent_bike(self):
        rent_bike_text = "Duration for rent : Rent of Bikes\n"
        for duration, rent in self.bikes_rent.items():
            rent_bike_text += f"{duration.capitalize()} : ₹ {rent}\n"
        return rent_bike_text

    def display_accept_return_bike(self, no_return_bike):
        self.bikes_available += no_return_bike
        return f"Now Available Bikes are: {self.bikes_available}"

    def display_discount_bike(self, customer_instance):
        total_amount = customer_instance.request_for_renting()
        discount_percentage = float(input("Discount percentage(%): "))

        discounted_amount = total_amount - (total_amount * (1 - discount_percentage / 100))
        print(f"\nDiscount applied: {discount_percentage}%")
        print(f"Discounted amount: ₹{discounted_amount}")
        return discounted_amount

    def display_bill_bike(self, customer_instance):
        customer_instance.bike_name = input("Enter the name of rented Bike: ")
        customer_instance.quantity = int(input("Enter Quantity: "))
        customer_instance.choice = input("Choose Duration for rent - \n1) Daily\n2) Weekly\n3) Monthly\n")

        total_amount = customer_instance.request_for_renting()
        discounted_amount = self.display_discount_bike(customer_instance)

        total_bill = total_amount - discounted_amount
        print("Final Total Bill", total_bill)

class Customer:
    def __init__(self):
        self.rented_bikes = {}
        self.total_amount = 0
        self.bike_name = None
        self.quantity = 0
        self.choice = None  # Initialize choice attribute

    def request_for_renting(self):
        duration_mapping = {"1": "Daily", "2": "Weekly", "3": "Monthly"}
        duration = duration_mapping.get(self.choice)
        if duration is None:
            print("Invalid choice")
            return 0

        return self.quantity * showroom_instance.bikes_rent[duration]

    def show_rented_bike_details(self):
        return f"Rented Bike \n milage: 340 \n speed limit: 120 km/hr \n code: BS16\n\n" \
               f"Rented Bike Name: {self.bike_name}\nQuantity: {self.quantity}\nDuration: {self.choice.capitalize()}"

def display_gui():
    window = tk.Tk()
    window.title("Bike Rental System")

    def display_available_bikes():
        available_bikes_text = showroom_instance.display_available_bikes()
        messagebox.showinfo("Available Bikes", available_bikes_text)

    def display_rent_bike():
        rent_bike_text = showroom_instance.display_rent_bike()
        messagebox.showinfo("Rent Bikes", rent_bike_text)

    def display_bill_bike():
        showroom_instance.display_bill_bike(customer_instance)

    def return_bike():
        no_return_bike = int(input("Number of returned bikes: "))  # Get this value from user input
        return_bike_text = showroom_instance.display_accept_return_bike(no_return_bike)
        print(return_bike_text)

    btn_available_bikes = tk.Button(window, text="Available Bikes", command=display_available_bikes)
    btn_available_bikes.pack()

    btn_rent_bike = tk.Button(window, text="Rent Bikes", command=display_rent_bike)
    btn_rent_bike.pack()

    btn_display_bill = tk.Button(window, text="Display Bill", command=display_bill_bike)
    btn_display_bill.pack()

    btn_return_bike = tk.Button(window, text="Return Bike", command=return_bike)
    btn_return_bike.pack()

    window.mainloop()

# Create instances
showroom_instance = BikeShowroom()
customer_instance = Customer()

# Display GUI
display_gui()