import os

print("CWD:", os.getcwd())

os.chdir("twelveth_day")

files = os.listdir()
print("Current directory files are:\n", files)
print(type(files))
print(len(files))


print("Python files in twelveth_day are:")
for f in files:
    if f.endswith(".py"):
        print(f)

try:
    os.mkdir("sample_dir")
    print("Directory sample_dir created...")
except FileExistsError:
    print("Directory sample_dir already exists...")

os.rename("sample_dir", "renamed_sample_dir")

# run any SYSTEM command
# DEPENDENT TO OS - Windows/Mac
os.system("open -a Pycharm")