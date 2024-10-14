'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''

def cost(qty):


    cp = 100

    cost = qty * cp

    if cost > 1000:

        total_cost = cost - (cost*(10/100))
    
    else:

        total_cost = cost


    return total_cost



qty = int(input("Enter the quantity in unit\t"))
print(f"The total cost is {cost(qty)}")