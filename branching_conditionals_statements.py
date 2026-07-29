import sys


name = sys.argv[1]
age = int(sys.argv[2])

if name == "preshaan":
    print("Welcome back ", name, "!")

print("Now checking if you could vote or not!")

if age >= 18 :
    print("Welcome ", name, " you can Vote!")
    print("This year the parties are: BJP, AAP, C, RC")
else:
    print("Nopes, ", name, " you can not vote this year!")
    print("You would need to wait for another ", 18 - age, " years")