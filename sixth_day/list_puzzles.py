# sum of number from x, y

# strictly not a multi-line comment but a string
# since not assigned it is as good as a comment
"""
x = 11
y = 20
numbers = list(range(x, y+1))
count = 0
for i in numbers:
    count += i

print("Sum of numbers from ", x, "to ", y, "is:", count)
# f strings - formatted strings - Python3.9+
print(f"Sum of numbers from {x} to {y} is: {count}")
"""

# =================
# from x to y, but only odd numbers
x = 11
y = 20
numbers = list(range(x, y+1))
count = 0
for i in numbers:
    # modulo operator
    # to get the remainder of an division operation
    if (i % 2) != 0:
        count += i

print(f"Sum of numbers from {x} to {y} is: {count}")

# list comprehension
numbers = [i for i in range(11, 21) if (i % 2) != 0]
print(f"numbers are: {numbers}")
s = sum(numbers)
print(f"Summation of these numbers are: {s}")

# =================
# min and max
# =================
numbers = [6,5,7,9,3,4,1,2,8]
low = min(numbers)
high = max(numbers)
print(f"Low and High in numbers are: {low}, {high}")

low_manual = sorted(numbers)[0]
high_manual = sorted(numbers)[-1]
high_manual = sorted(numbers, reverse=True)[0]
print(f"Low and High in numbers are: {low}, {high}")
