from date_utils_Q6 import calculations_Q6 as cal


print("Enter the first date (DD/MM/YYYY):")
date1_str = input()
print("Enter the second date (DD/MM/YYYY):")
date2_str = input()


date1 = tuple(map(int, date1_str.split("/")))
date2 = tuple(map(int, date2_str.split("/")))


days_diff = cal.days_between(date1, date2)
print(f"Number of days between {date1} and {date2}: {days_diff}")

# Add days to the first date
print("Enter the number of days to add to the first date:")
days_to_add = int(input())

new_date = cal.add_days(date1, days_to_add)
print(f"The new date after adding {days_to_add} days is: {new_date[0]:02}/{new_date[1]:02}/{new_date[2]}")