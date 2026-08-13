s1 = "Some text to write in a file. appended"

# mode
# w - write
# w+ - write with cleaning it first
# a - append at the end, file should exist
# a+ - append at the end, file if not exist, would be created
# r - read
f = open("some_out.txt", "w")
f.write(s1 + "\n")
f.close()

