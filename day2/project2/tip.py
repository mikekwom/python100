from shlex import split


print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))

tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

split_num = int(input("How many people will split the bill? "))

final_total = total * (100 / tip_percent) / split_num
format_total = str("{:.2f}".format(final_total))

print("Each person should pay: $" + format_total)