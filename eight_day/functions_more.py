def add_numbers(n1=0, n2=0):
    print(f"addition of {n1} and {n2} is:", n1+n2)
    return n1+n2

r = add_numbers(10, 20)
print(f"Sum is: {r}")

r = add_numbers(10)
print(f"Sum is: {r}")

r = add_numbers()
print(f"Sum is: {r}")

def sub_numbers(n1, n2):
    print(f"subtraction of {n1} and {n2} is:", n1-n2)
    return n1-n2

def add_all_numbers(n1, n2=0, n3=0, n4=0, n5=0):
    print("Add of numbers are: ", n1+n2+n3+n4+n5)
    return n1+n2+n3+n4+n5

r = sub_numbers(n2=20, n1=10)
print(f"Diff is: {r}")

r = add_all_numbers(10)
print(f"Sum is: {r}")

# wont work, bcoz n1 is not given
# r = add_all_numbers(n3=10)

# works bcoz n1 is given using positional args
r = add_all_numbers(10, n3=20)

# works bcoz n1 is given using keyword/named args
# r = add_all_numbers(n1=10, n3=20)
print(f"Sum is: {r}")

