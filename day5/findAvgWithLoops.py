# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
totalHeight = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

for height in student_heights:
  totalHeight += height
  
avgHeight = round(totalHeight / len(student_heights))
print(f"Avg height of students: {avgHeight}")

# find number of students
studentTotal = 0
for student in student_heights:
  studentTotal += 1
print(f"Total number of students: {studentTotal}")