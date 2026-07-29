# if else if ladder
# else if is called elif in short in Python
# else is optional
import sys

marks = int(sys.argv[1])

grade = "F"

# This is first case, but faulty
# if marks >= 95:
#     grade = "A+"
# if marks >= 85:
#     grade = "A"
# if marks >= 75:
#     grade = "B+"
# if marks >= 65:
#     grade = "B"

# one way of doing it
# if marks >= 95:
#     grade = "A+"
# if marks >= 85 and marks < 95:
#     grade = "A"
# if marks >= 75 and marks < 85:
#     grade = "B+"
# if marks >= 65 and marks < 75:
#     grade = "B"


# better way of doing it
if marks >= 95:
    grade = "A+"
elif marks >= 85:
    grade = "A"
elif marks >= 75:
    grade = "B+"
elif marks >= 65:
    grade = "B"
# else:
#     grade = "Z"


print("Your grades are: ", grade)