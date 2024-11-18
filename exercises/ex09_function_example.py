# Create a code that calculates the amount to be paid for the purchase
# of a number of pieces (determined by the user),
# with a different discount depending on the desired quantity

def calculate_discount(price, quantity, discount):
	"""
	Calculate the discount and the total price to pay
	:param price: float
	:param quantity: int
	:param discount: float
	:return: tuple
	"""
	discount = discount / 100
	total_price = price * quantity
	discounted_price = total_price * discount
	return (discounted_price, total_price - discounted_price)

while True:
	nb_pieces = int(input("Enter the number of pieces: "))
	if nb_pieces > 0:
		break
piece_price = 189.99

if nb_pieces < 100:
	discount = 0
	discount, total = calculate_discount(piece_price, nb_pieces, discount)
elif ((100 < nb_pieces) and (nb_pieces < 1000)):
	discount = 5
	discount, total = calculate_discount(piece_price, nb_pieces, discount)
else:
	discount = 10
	discount, total = calculate_discount(piece_price, nb_pieces, discount)
print(f"Total price to pay is {total} $ and the discount is {discount} $")
