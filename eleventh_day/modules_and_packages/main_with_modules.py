import myfuncs
import myfuncs as mf
from myfuncs import greet

# This is the best used approach - guidelines
from myfuncs import greet as mygreet

print("Hello from main.py!")
myfuncs.greet("Preshaan")
mf.greet("Abhijit")
greet("Aakash")
mygreet("Prakash")