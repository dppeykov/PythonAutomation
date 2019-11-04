# GOOD RESOURCES: https://www.programiz.com/python-programming/methods/built-in/open
# https://www.programiz.com/python-programming/file-operation

# READING FILES:

# f = open('data.txt', 'r')
# print(f.read())  # will iterate through the file and read all lines
# f.close()

# file_input = open('data.txt', 'r')
# for line in file_input:
#     line_split = line.split()
#     if line_split[2] == "P":
#         print(line)
# file_input.close()

# WRITING TO FILES:

f = open('data.txt', 'r')
passFile = open('pass_file.txt', 'w')
failFile = open('fail_file.txt', 'w')
for line in f:
    if line.split()[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()

# The best way to do this is using the with statement. 
# This ensures that the file is closed when the block inside with is exited.

# We don't need to explicitly call the close() method. It is done internally.

#with open("test.txt",encoding = 'utf-8') as f:
  # perform file operations
