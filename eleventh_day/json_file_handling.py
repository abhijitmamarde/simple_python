import json

data = json.load(open("sample_input.json", "r"))
print(f"Loaded data is: {data}")

f2 = open("sample_input.json", "r")
data = json.load(f2)
f2.close()
print(f"Loaded data is: {data}")

with open("sample_input.json", "r") as f3:
    data = json.load(f3)
    print(f"Loaded data is: {data}")

data2 = [{'name': 'preshaan', 'phone': 1234, 'age': 18, 'classes': ['eng', 'computer', 'maths', 34], 'have_glasses': True, 'hobbies': None}, {'name': 'abhi', 'age': 28, 'have_glasses': False}]
json.dump(data2, open("sample_output.json", "w"), indent=4)

# Assignment 1:
# do similar way with write as done in Line #6 and Line #11 for read

# Assignment 2:
# Write a program to take any CSV filename as input and output the JSON equivalent of it

# Assignment 3:
# Write a program to take any JSON filename as input and output the CSV file equivalent of it
