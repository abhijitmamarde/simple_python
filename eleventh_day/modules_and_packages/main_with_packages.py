import myutils.hello as mf
from myutils.hello import greet

# This is the best used approach - guidelines
from myutils.hello import greet as mygreet

# for add
import myutils.maths as m
from myutils.maths import add

# This is the best used approach - guidelines
from myutils.maths import add as myadd

print("Hello from main.py!")
mf.greet("Abhijit")
greet("Aakash")
mygreet("Prakash")

print("sum is:", m.add(2, 5))
print("sum is:", add(2, 5))
print("sum is:", myadd(2, 5))


# assignment do same for sub, add more funcs too and use it