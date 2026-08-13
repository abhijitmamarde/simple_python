def print_my_name():
    print("My name is Preshaan")
    for i in range(1, 6):
        print(f"I is {i}")

def print_my_custom_name(name):
    print(f"My name is {name}")
    for i in range(1, 6):
        print(f"I is {i}")

# TypeError: add_numbers() missing 1 required positional argument: 'n3'
# def add_numbers(n1, n2, n3):

# TypeError: add_numbers() takes 1 positional argument but 2 were given
# def add_numbers(n1):

def add_numbers(n1, n2):
    print(f"addition of {n1} and {n2} is:", n1+n2)
    return n1+n2

def add_and_sub_numbers(n1, n2):
    print(f"addition of {n1} and {n2} is:", n1+n2)
    print(f"subtraction of {n1} and {n2} is:", n1-n2)
    return n1+n2, n1-n2




print("This is first line")
print_my_name()
print("This is another line")
print_my_name()
print("This is last line")
print_my_custom_name("Abhijit")
print_my_custom_name("Preshaan")
print_my_custom_name("")

sum1 = add_numbers(10, 23)
print(f"Sum1 is: {sum1}")
add_numbers(sum1, 100)

a, s = add_and_sub_numbers(10, 23)
add_and_sub_numbers(a, s)

t = add_and_sub_numbers(10, 23)
print(f"Type of return is: {type(t)}")