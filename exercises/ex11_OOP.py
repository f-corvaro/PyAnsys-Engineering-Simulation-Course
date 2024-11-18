# An exercise to understand the basics of OOP in Python

class Car:
	"""
    A class to represent a car.

    Attributes:
    make (str): The make of the car.
    model (str): The model of the car.
    year (int): The year the car was manufactured.
    price (float): The price of the car.
    """
	def __init__(self, make: str, model: str, year: int, price: float):
		"""
        Constructs all the necessary attributes for the car object.

        Parameters:
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The price of the car.
        """
		self.make = make
		self.model = model
		self.year = year
		self.price = price

	def get_description(self):
		"""
        Prints a description of the car.
        """
		print(f"This car is a {self.year} {self.make} {self.model}.")

	def price_request(self):
		"""
        Prints the price of the car.
        """
		print(f"The price is: {self.price}$")

	def monthly_payment(self, months: int):
		"""
        Calculates and prints the monthly payment for the car.

        Parameters:
        months (int): The number of months over which the payment will be made.
        """
		monthly_payment = self.price / months
		print(f"The monthly payment is: {monthly_payment}$ for {months} months.")

# Creating instances of the Car class
car1 = Car(make="Toyota", model="Corolla", year=2021, price=20000)
car1.get_description()
car1.price_request()
car1.monthly_payment(months=24)

car2 = Car("Toyota", "Supra", 2000, 150000)
car2.get_description()
car2.price_request()
car2.monthly_payment(24)