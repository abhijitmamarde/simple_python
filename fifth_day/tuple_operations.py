t = (1, 2, 3)
print("Type of t is:", type(t))

# accessing eleme at index pos
print("first elem:", t[0])
print("last elem:", t[2])
print("last elem:", t[-1])
print("last elem:", t[len(t)-1])

for i in t:
    print(i)

count = 0
for i in t:
    count += i
print("Sum is:", count)


# this dont work
# AttributeError: 'tuple' object has no attribute 'append'
# t.append(5)

# t.insert
# t.sort()
# t.reverse()
# t.clear()
# t.remove()

print("2 found count:", t.count(2))

# tuple to list or vv
t = (1, 2, 3)
l = list(t)
print("t was:", t)
print("l is:", l)

# list to tuple
l = [1, 2, 3]
t = tuple(l)
print("l was:", l)
print("t is:", t)

# list updated after converting from tuple
# tuple is not changed
t = (1, 2, 3)
l = list(t)
l.append(4)
print("t was:", t)
print("l is:", l)

# use range to create tuple
# t = (1, 2, 3, ... 10)
t = tuple(list(range(1, 11)))
t = tuple(range(1, 11))
print("t is:", t)
