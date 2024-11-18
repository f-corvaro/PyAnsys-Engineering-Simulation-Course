# This program is to demonstrate the use of conditional statements in Python

x = float(input("Enter a number, x: "))
y = float(input("Enter a number, y: "))

if x < y:
    print("x:", x, " is less than y:", y)
elif x == y:
    print("x:", x, "is equal to y:", y)
else:
    print("x:", x, " is greater than y:", y)

print("x is equal to y?", x==y)