# CSV - comma seprated values
# Table of rows and cols
# May or may not have column names / header names

# CSV file format is supported natively in Python very well

data = [
    {'name': 'Presshaan', 'phone': '12345', 'marks': '98'},
    {'name': 'Abhijit', 'phone': '223344', 'marks': 95},
    {'name': 'Aakash', 'phone': '333444', 'marks': '93'},
]

# first approach - basic ====================================
f = open("sample_out.csv", "w")
f.write("name,phone,marks\n")

for d in data:
    f.write(f"{d['name']},{d['phone']},{d['marks']}\n")

f.close()

# second approach - usng csv writer ====================================

import csv 

with open('sample_out2.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'phone', 'marks']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    # for d in data:
    #     writer.writerow(d)
    writer.writerows(data)


csvfile = open('sample_out2.csv', 'w', newline='')
fieldnames = ['name', 'phone', 'marks']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

writer.writeheader()
# for d in data:
#     writer.writerow(d)
writer.writerows(data)

csvfile.close()