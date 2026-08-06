d1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
}

for k,v in d1.items():
    if v % 2 != 0:
        print(k, v)

i = 0

while i in range(0, len(d1)):
    k = list(d1.keys())[i]
    v = list(d1.values())[i]   
    if v % 2 != 0:
        print(k, v)     
    i += 1
