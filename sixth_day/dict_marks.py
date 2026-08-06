"""
We need to provide analysis of marks got in one subject for an entire class

Student name which scored highest in the class along with the marks:
Student name which scored lowest in the class along with the marks:
count of passing students (>=35) along with their names:
count of failing students (<=35) along with their names:

Student names who scored higher than the total class average (Average in the class).
"""

# class_marks = [
#     ["preshaan", 91],
#     ["aaa", 99],
#     ["bbb", 90],
# ]

class_marks = [
    [91, "preshaan"],
    [99, "aaa"],
    [99, "bbb"],
]

max_marks = max(class_marks)
print(f"Max Marks are: {max_marks}")

min_marks = min(class_marks)
print(f"Min Marks are: {min_marks}")

# =======================
class_marks = {
    
    # "preshaan": 91,
    "aaa": 92,
    "bbb": 99,
    "preshaan": 91,
    
}

max_marks = 0
max_student_name = []
for k, v in class_marks.items():
    if max_marks < v:
        max_marks = v
        max_student_name.clear()
    if max_marks == v:
        max_student_name.append(k)
print(f"Student who scored highest: {max_student_name} and marks got is: {max_marks}")
