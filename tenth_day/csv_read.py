import csv

with open('sample_input.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)


def get_low_and_high(lines):
    h = 0
    h_name = ""
    l = 100
    l_name = ""

    for data in lines:
        k = data["name"]
        v = int(data["marks"])

        if h < v:
            h = v
            h_name = k
        if l > v:
            l = v
            l_name = k

    print("Highest mark stud is: ", h_name) 
    print("Lowest mark stud is: ", l_name) 


print("Using Dictreader...")

with open('sample_input.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    get_low_and_high(csvreader)
    # for row in csvreader:
    #     # print(row['name'], row['marks'])
    #     print(row)