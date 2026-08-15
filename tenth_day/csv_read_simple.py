f = open("sample_input.csv", "r")
s = f.read()
f.close()

print(s)

# print name of students with highest and lowest marks
def get_low_and_high(d):
    h = 0
    h_name = ""
    l = 100
    l_name = ""

    for k, v in d.items():
        if h < v:
            h = v
            h_name = k
        if l > v:
            l = v
            l_name = k


    print("Highest mark stud is: ", h_name) 
    print("Lowest mark stud is: ", l_name) 

d = {
    "aaa": 100,
    "bbb": 99,
    "ccc": 98,
}

get_low_and_high(d)

d2 = {}
lines = s.split("\n")
for l in lines:
    # print(l)
    fields = l.split(",")
    print(fields)
    if (fields[0] != "name") and (fields[0] != ""):
        print("Inside!!!")
        d2[fields[0]] = int(fields[-1])

print(f"read dict is: {d2}")
get_low_and_high(d2)

