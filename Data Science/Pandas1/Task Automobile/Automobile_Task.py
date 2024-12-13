import pandas as pd


df = pd.read_csv("C:/Users/anuru/OneDrive/Desktop/Luminar DSML/Data Science/Pandas1/Task Automobile/Automobile_data.csv")


# 1. From the given dataset print the first and last five rows

print("1. From the given dataset print the first and last five rows")
print(df.head(5))
print("-"*100)
print(df.tail(5))

print("*"*100)

# 2. Find the missing values and Check if there is any duplicate values
print("2. Find the missing values and Check if there is any duplicate values")
print(df.isna().sum())
print("-"*100)
print(df.duplicated().sum())
print("*"*100)

# 3. Print All Toyota Cars details
print("3. Print All Toyota Cars details")
print(df.loc[df['company'] == 'toyota'])
print("*"*100)

# 4. Count total cars per company
print("4. Count total cars per company")
print(df.groupby('company')['company'].count())
print("*"*100)

# 5. Find each company’s Highest price car
print("5. Find each company’s Highest price car")
max_price = df.groupby('company')['price'].max()
new = pd.merge(df,max_price,on=['company','price'],how='inner')
print(new)
print("*"*100)

# 6. Find the average mileage of each car making company
print("6. Find the average mileage of each car making company")
print(df.groupby('company')['average-mileage'].mean())
print("*"*100)

# 7. Sort all cars by Price column
print("7. Sort all cars by Price column")
print(df.sort_values('price'))
print("*"*100)

# 8. Sort all cars by Price column
print("8. Sort all cars by Price column(desc)")
print(df.sort_values('price',ascending = False))
print("*"*100)

# 9. Concatenate two data frames using the following condition
"""
Create two data frames using the following two dictionaries.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan',
'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]
"""
print("9. Concatenate two data frames using the following condition")

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan',
'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
german = pd.DataFrame(GermanCars)
japanese = pd.DataFrame(japaneseCars)
cars = pd.concat([german,japanese],keys=['Germany','Japan'])
print(cars)
print("*"*100)

# 10. Merge two data frames using the following condition
print("10. Merge two data frames using the following condition")
"""
Create two data frames using the following two Dicts, Merge two
data frames, and append the second data frame as a new column to
the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'horsepower': [141, 80, 182 , 160]}
"""
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
'horsepower': [141, 80, 182 , 160]}

cars = pd.DataFrame(Car_Price)
horse = pd.DataFrame(car_Horsepower)
new = cars.merge(horse,on='Company',how='inner')
print(new)



