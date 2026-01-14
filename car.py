class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display(self):
        print(self.year, self.make, self.model, "- Price:", self.price)


n = int(input("How many cars want to enter? "))
cars = []

for i in range(n):
    print(f"\nEnter details of Car {i+1}:")
    make = input("Enter Make/Brand: ")
    model = input("Enter Model: ")
    year = int(input("Enter Year: "))
    price = float(input("Enter Price: "))
    
    cars.append(Car(make, model, year, price))

limit = float(input("\nEnter the starting price: "))
print(f"\nCars with price greater than {limit} is:\n")

for c in cars:
    if c.price > limit:
        c.display()