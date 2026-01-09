import tkinter as tk
from tkinter import ttk, messagebox

# ================= BUSINESS LOGIC =================
class BikeShowroom:
    def __init__(self):
        self.bikes = {
            "Royal Enfield": 10,
            "Honda SP 125": 20,
            "Hero Splendor Plus": 25,
            "TVS Raider": 10,
            "Yamaha": 15,
            "Kawasaki": 5,
            "Ducati": 10
        }
        self.rent = {"Daily": 100, "Weekly": 600, "Monthly": 2500}

    def calculate_bill(self, qty, duration, discount):
        total = self.rent[duration] * qty
        return total - (total * discount / 100)

    def bikes_text(self):
        return "\n".join(f"{b} : {q}" for b, q in self.bikes.items())


# ================= GUI =================
class BikeRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike Rental System")
        self.root.geometry("900x560")
        self.root.configure(bg="#F4F6F7")

        self.showroom = BikeShowroom()
        self.setup_style()
        self.build_ui()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Header.TLabel",
                        background="#0B3C49",
                        foreground="white",
                        font=("Segoe UI", 24, "bold"))

        style.configure("Card.TFrame",
                        background="#FFFFFF",
                        relief="flat")

        style.configure("Title.TLabel",
                        background="#FFFFFF",
                        foreground="#2C3E50",
                        font=("Segoe UI", 15, "bold"))

        style.configure("TButton",
                        background="#1ABC9C",
                        foreground="white",
                        font=("Segoe UI", 11),
                        padding=10)

        style.map("TButton",
                  background=[("active", "#16A085")])

        style.configure("Accent.TButton",
                        background="#F39C12",
                        foreground="white")

        style.map("Accent.TButton",
                  background=[("active", "#E67E22")])

    def build_ui(self):
        # Header
        header = ttk.Label(self.root, text="🏍 Bike Rental Showroom",
                           style="Header.TLabel", anchor="center")
        header.pack(fill="x", ipady=18)

        main = tk.Frame(self.root, bg="#F4F6F7")
        main.pack(fill="both", expand=True, padx=25, pady=25)

        # Left Card
        left = ttk.Frame(main, style="Card.TFrame")
        left.grid(row=0, column=0, sticky="nsew", padx=15)

        ttk.Label(left, text="Rent Your Bike", style="Title.TLabel")\
            .grid(row=0, column=0, columnspan=3, pady=15)

        ttk.Label(left, text="Bike Model").grid(row=1, column=0, sticky="w", pady=8)
        self.bike = ttk.Combobox(left, values=list(self.showroom.bikes.keys()),
                                 state="readonly", width=22)
        self.bike.current(0)
        self.bike.grid(row=1, column=1)

        ttk.Label(left, text="Quantity").grid(row=2, column=0, sticky="w", pady=8)
        self.qty = ttk.Entry(left, width=24)
        self.qty.insert(0, "1")
        self.qty.grid(row=2, column=1)

        ttk.Label(left, text="Duration").grid(row=3, column=0, sticky="w", pady=8)
        self.duration = tk.StringVar(value="Daily")
        for i, d in enumerate(["Daily", "Weekly", "Monthly"]):
            ttk.Radiobutton(left, text=d, variable=self.duration, value=d)\
                .grid(row=3, column=1+i, padx=4)

        ttk.Label(left, text="Discount (%)").grid(row=4, column=0, sticky="w", pady=8)
        self.discount = ttk.Entry(left, width=24)
        self.discount.insert(0, "0")
        self.discount.grid(row=4, column=1)

        ttk.Button(left, text="Generate Bill",
                   command=self.generate_bill)\
            .grid(row=5, column=0, columnspan=3, pady=20)

        # Right Card
        right = ttk.Frame(main, style="Card.TFrame")
        right.grid(row=0, column=1, sticky="nsew", padx=15)

        ttk.Label(right, text="Bill Summary", style="Title.TLabel").pack(pady=15)

        self.output = tk.Text(right, height=15, width=42,
                              bg="#ECF0F1", fg="#2C3E50",
                              font=("Consolas", 11),
                              bd=0)
        self.output.pack(padx=15, pady=10)

        ttk.Button(right, text="Show Available Bikes",
                   style="Accent.TButton",
                   command=self.show_bikes)\
            .pack(pady=10)

    def generate_bill(self):
        try:
            qty = int(self.qty.get())
            discount = float(self.discount.get())
            total = self.showroom.calculate_bill(qty, self.duration.get(), discount)

            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END,
                               f"Bike Model: {self.bike.get()}\n"
                               f"Quantity: {qty}\n"
                               f"Duration: {self.duration.get()}\n"
                               f"Discount: {discount}%\n"
                               f"------------------------------\n"
                               f"TOTAL BILL: ₹ {total:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter valid numeric values")

    def show_bikes(self):
        messagebox.showinfo("Available Bikes", self.showroom.bikes_text())


# ================= RUN =================
root = tk.Tk()
BikeRentalApp(root)
root.mainloop()
