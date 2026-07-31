result = 1 + 2 + 3
print("Addition from 1 to 3 is ", result)

start_number = 1
end_number = 4
# result = 1 + 2 + 3 + 4 + 5 + 6 ... 30

# range function 1st number is included, 2nd number is Excluded
count = 0
for i in range(start_number, end_number):
    count += i

print("Addition from ",start_number," to ", end_number, " is ", count)


print(range(1, 4))
print("range(1, 4)")

# 1, 2 .. 10
for i in range(1, 11):
    print(i)

# 1, 3, 5 .. 9
for i in range(1, 11, 2):
    print(i)

# 10, 9, ... 1
for i in range(10, 0, -1):
    print(i)

# WAP which will print numbers 
# 1 to 100 in descending order, 
# 101 to 200 in ascending order, 
# 201 to 300 in descending order,

