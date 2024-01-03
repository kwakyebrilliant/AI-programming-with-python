# f = open('some_file.txt', 'r')
# file_data = f.read()
# f.close()

# print(file_data)

# f = open('another_file.txt', 'w')
# f.write('Hello World!')
# f.close

with open('another_file.txt', 'r') as f:
    file_data = f.read()