# l = [1, 2, 3, ... 10]
l = list(range(1, 11))

# l = [10, 9, 8, ... 1]
l = list(range(10, 0, -1))

l = list(range(100, 0, -1))

print(l)

# for i in range()
for i in l:
    print(i)

count = 0
for i in l:
    count += i
print("Sum is:", count)

count = (l[0] + l[-1]) * (len(l) // 2)
print("Sum is:", count)

# --------------
l = [1,2,3,2,4,3,1,2]
# count how many times an value is coming in list
print(l.count(2))

# remove all items from list
l.clear()
print(l)

# sort an list
l = [1,2,3,2,4,3,1,2]
l.sort()
print(l)

# sorted
l = [1,2,3,2,4,3,1,2]
sl = sorted(l)
print(l) # not sorted
print(sl) # sorted

# sort but in reverse/descending
l = [1,2,3,2,4,3,1,2]
# l.sort(reverse=True)
sl = sorted(l, reverse=True)
print("Before Reverse sort:", l) # not sorted
print("After Reverse sort:",sl) # sorted in reverse

# reveres
l = [1,2,3,2,4,3,1,2]
print("Before reverese", l)
l.reverse()
print("After reverese",l)

# ------------------------------------------

l = [1, 2, 3, 4, 5]
print("l is:", l)
l.remove(4)
print("l after removing value 4:", l)