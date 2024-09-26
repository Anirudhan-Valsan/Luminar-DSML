#>100000    - 15%
# 50000 to 100000(inclusive) -  10%
# <=50000     -   5%

price=int(input("Enter the price\n"))

if price>50000 and price<=100000:
    tax=price* 10/100
elif price>100000:
    tax=price* 15/100
else:
    tax=price* 5/100

print(f"The tax for the price{price} is {tax}")