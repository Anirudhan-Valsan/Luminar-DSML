def my_discount():
    price = float(input("Enter the price: "))
    disc = float(input("Enter the discount percentage: "))
    return price - (price * (disc / 100))

print('The price after discount:', my_discount())
