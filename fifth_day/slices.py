# slice as apple slice
l1 = list(range(1, 21))
# [ 1, 2, 3, 4, 5, ...., 20]
l2 = l1[1:3] # similar to range, 1st parameter is inclusive, 2nd is exclusive
print("l2 is:", l2)
print("type of l2 is:", type(l2))

l1 = tuple(range(1, 21))
# ( 1, 2, 3, 4, 5, ...., 20)
l2 = l1[1:3] # similar to range, 1st parameter is inclusive, 2nd is exclusive
print("l2 is:", l2)
print("type of l2 is:", type(l2))

l1 = list(range(1, 21))
# [ 1, 2, 3, 4, 5, ...., 20]
l2 = l1[1:-3:2] # similar to range, 1st parameter is inclusive, 2nd is exclusive
print("l2 is:", l2)
print("type of l2 is:", type(l2))

l1 = list(range(1, 21))
l2 = l1[::] # exactly same as l1
# l2 = l1[::-1] # exactly reverse of l1
print(l1)
print(l2)