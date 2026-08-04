"""
We need to provide analysis of marks got in one subject for an entire class

Max marks got:
Lowest marks got:
count of passing students (>=35):
count of failing students (>=35):
Average in the class
"""

class_marks = [99, 88, 67, 35, 19, 11, 30, 75]
max_marks = max(class_marks)
lowest_marks = min(class_marks)
print(f"Highest marks are: {max_marks}")
print(f"Lowest marks are: {lowest_marks}")

# count of passing student
count = 0
for marks in class_marks:
    if marks >= 35:
        count += 1
print(f"Count of students which are passed: {count}") 

# count of failing student
count = 0
for marks in class_marks:
    if marks < 35:
        count += 1
print(f"Count of students which are failed: {count}") 

# Average of class marks
avg_marks = sum(class_marks) / len(class_marks)
print(f"Average class marks are: {avg_marks}") 

