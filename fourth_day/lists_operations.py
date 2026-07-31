l = [1, 2, 3]
print("l is:", l)

# accessing elements with index using square operator, index operator, loc op
# array indexing starts with 0
print("first element in l is:", l[0])
print("second element in l is:", l[1])
print("third element in l is:", l[2])

# IndexError: list index out of range
# print("fourth element in l is:", l[3])

print("Lenght of l is:", len(l))
print("last element in l is:", l[len(l)-1])

# negative index positions, always work along with len
print("last element in l is:", l[-1])

print("second last element in l is:", l[-2])
print("third last element in l is:", l[-3])

# IndexError: list index out of range
# print("fourth last element in l is:", l[-4])

l[2] = "added"
print(l)

l.append("one more value")
print(l)

# [1, 2, 'added', 'one more value'] --> first added at 0th index pos
# create new slot at index pos 0, rest everything will be sfifted to left
# 
# ['first', 1, 2, 'added', 'one more value']
l.insert(0, "first")
print(l)

l.insert(-1, "Where this goes?")
print(l)
