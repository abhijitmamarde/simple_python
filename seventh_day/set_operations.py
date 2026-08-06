s1 = {1, 2, 3, 2, 3, 0, 9, 3}
# s2 = {2, 3, 4, 6}
s2 = {2, 3, 4, 6}

print(s1)
print(len(s1))

for i in s1:
    print(i)

print(f"Set 1 is: {s1}")
print(f"Set 2 is: {s2}")


print("Difference is:", s1.difference(s2))
print("Intersection is:", s1.intersection(s2))

print("Is Subset?", s1.issubset(s2))
print("Is Superset?", s1.issuperset(s2))

# s1.clear()

# not available
# calling sort function OF object type set
# s1.sort()

# This is a function
s1_rev = sorted(s1, reverse=True)
print("Reverse sort of s1 is:", s1_rev)

# for set this is not possible
# print("First element is:", s1[0])

"""
Lets say we have 10 lists of topper names for 10 diff subjects

Take User Input of subject name: s1, s2, s9
Show who are the common toppers from this subject
"""
