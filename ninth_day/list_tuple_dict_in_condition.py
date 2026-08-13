l1 = list(range(1, 11))

n = 5
for i in l1:
    if i == n:
        print(f"Number {n} is present in l1")
    else:
        print(f"Number {n} is not present in l1")

for i in l1:
    if i == n:
        print(f"Number {n} is present in l1")
        break
    else:
        print(f"Number {n} is not present in l1")

print("================== 3 =================")
for i in l1:
    if i != n:
        continue
    print(f"Number {n} is present in l1")
    break

print("================== 4 =================")
for index, i in enumerate(l1):
    if i != n:
        continue
    print(f"Number {n} is present in l1 at index: {index}")
    break

if n in l1:
    index = l1.index(n)
    print(f"Number {n} is present in l1")
    print(f"Number {n} is present in l1 at index: {index}")

d = {
    "preshaan": 98,
    "abhi": 96,
    "aaa": 88,
    "bbb": 89,
    "ccc": 86,
}

print("checking for aaa: ", "aaa" in d)
print("checking for ccc: ", "ccc" in d)
print("checking for eee: ", "eee" in d)

print("checking for Value 96 in d: ", 96 in d.values())
print("checking for Value 86 in d: ", 86 in d.values())
print("checking for Value 99 in d: ", 99 in d.values())

s1 = "Abhijit"
s2 = "Preshaan"

print("i in s1:", "i" in s1)
print("i in s2:", "i" in s2)

# split and joins in string
s1 = "Abhi,Preshaan,aaa,bbb,ccc"

names = s1.split(",")
print("names are:", names)

joined_names = ",".join(names)
print("joined names are:", joined_names)
