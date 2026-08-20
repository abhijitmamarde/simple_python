def sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print("sum till 5: ", sum(5))
print("sum till 10: ", sum(10))
print("sum till 100: ", sum(100))
print("sum till 100000: ", sum(100000))

# Recurrsion means - function calling itself
# Stopping condition

def r_sum(n):
    if n == 1:
        return 1
    else:
        return n + r_sum(n-1)

print("rsum till 5: ", r_sum(5))
print("rsum till 10: ", r_sum(10))
print("rsum till 100: ", r_sum(100))
# RecursionError: maximum recursion depth exceeded
# print("rsum till 100000: ", r_sum(100000))

# Fibonacci series calculation
# 0,1,1,2,3,5,8,13,21,34, ...
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print("5th term:", fibonacci(5))
print("9th term:", fibonacci(9))
print("10th term:", fibonacci(10))

# Assignment - do it without using recurssion