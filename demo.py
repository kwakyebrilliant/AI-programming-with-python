# try:
#     x = int(input('Enter a number: '))
# except:
#     print('That\s not a valid number')

# while True:
#     try:
#         x = int(input('Enter a number: '))
#         break
#     except:
#         print('\nAtempted Input\n')
#     finally:
#         print('\nAtempted Input\n')

f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)