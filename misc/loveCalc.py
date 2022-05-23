# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

combined_str = name1 + name2
lower_combined_str = str(combined_str)

col1_total = 0
col2_total = 0

col1_total += lower_combined_str.count("t")
col1_total += lower_combined_str.count("r")
col1_total += lower_combined_str.count("u")
col1_total += lower_combined_str.count("e")

col2_total += lower_combined_str.count("l")
col2_total += lower_combined_str.count("o")
col2_total += lower_combined_str.count("v")
col2_total += lower_combined_str.count("e")


str_total = int(str(col1_total) + str(col2_total))

if str_total < 10 or str_total > 90:
  print(f"You score is {str_total}, you go together like coke and mentos.")
elif str_total >= 40 and str_total <= 50:
  print(f"You score is {str_total}, you are alright together.")
else:
  print(f"Your score is {str_total}.")