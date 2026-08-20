import sys
print(f"System Path is: {sys.path}")
# needs the path for my_other_utils in PYTHONPATH env variable
import my_other_utils as u

u.hello("Preshaan")