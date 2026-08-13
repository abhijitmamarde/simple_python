def add_numbers(l):
    sum = 0
    for n in l:
        sum += n
    print("Sum is:", sum)
    return sum

# int is not itreable
# add_numbers(1)
add_numbers([1, 2, 3])
add_numbers((1, 2, 3))
add_numbers({1, 2, 3})

def append(l, v):
    l.append(v)
    print(f"Append {v} to the list, the list is: {l}")
    return l

def append2(l, v):
    rl = l[:]
    rl.append(v)
    print(f"Append {v} to the list, the list is: {rl}")
    return rl

l1 = [1, 2, 3]
append(l1, 90)
print(f"after append the list is: {l1}")

append(l1, 100)
print(f"after append the list is: {l1}")

l1 = [1, 2, 3]
l2 = append2(l1, 90)
print(f"after append2 the list is: {l2}")
print(f"original list is: {l1}")

l3 = append2(l2, 100)
print(f"after append2 the list is: {l3}")
print(f"original list is: {l1}")


# the gotcha with default list
def append_v3(l=[], v=1):
    l.append(v)
    print(f"Append {v} to the list, the list is: {l}")
    return l

def append_v4(l=None, v=1):
    if l is None:
        l = []
    l.append(v)
    print(f"Append {v} to the list, the list is: {l}")
    return l

rl = append_v3()
print(f"after append the list is: {rl}")

rl = append_v3()
print(f"after append the list is: {rl}")

rl = append_v3(v=98)
print(f"after append the list is: {rl}")

rl = append_v3(v=99)
print(f"after append the list is: {rl}")

rl = append_v3(v=100, l=[])
print(f"after append the list is: {rl}")

print("============ v4 calling now ===============")
rl = append_v4()
print(f"after append the list is: {rl}")

rl = append_v4()
print(f"after append the list is: {rl}")

rl = append_v4(v=98)
print(f"after append the list is: {rl}")

rl = append_v4(v=99)
print(f"after append the list is: {rl}")

rl = append_v4(v=100, l=[])
print(f"after append the list is: {rl}")