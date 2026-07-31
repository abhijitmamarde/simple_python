# basic types int, float, string, bool, None
i = 10
f = 10.0
s = ""

print("i is: ", i, " type is: ", type(i))
print("f is: ", f, " type is: ", type(f))
print("s is: ", s, " type is: ", type(s))

# adv types - those are based on some data structures
# list - collection of objects / values
# arrays - list and arrays are same EXCEPT in list we can have values of diff types

l = []
print("l is: ", l, " type is: ", type(l))

l = [1, 2, 4, 3]
print("l is: ", l, " type is: ", type(l))

l = [1, 2, 4, 3, 3.5, True, None, "abc", ["one", "tweo", "three"]]
print("l is: ", l, " type is: ", type(l))

# ================ tuple: read only version of list
t = (1, 2, 4)
print("t is: ", t, " type is: ", type(t))

t = (1, 2, 4, 3, 3.5, True, None, "abc", ["one", "tweo", "three"])
print("t is: ", t, " type is: ", type(t))

# ================ dict - dictionary - key value structure
d = {}
print("d is: ", d, " type is: ", type(d))

d = {"preeshan": 78, "abhi": 75}
print("d is: ", d, " type is: ", type(d))

# =============== set - similar to list but can not have duplicate values
s = set([1, 2, 3])
print("s is: ", s, " type is: ", type(s))

s = set([1, 2, 2, 4, 4, 2, 1, 3])
print("s is: ", s, " type is: ", type(s))

print(set([1, 2, 3, 2]))
print(set([1, 3, 3, 2]))
