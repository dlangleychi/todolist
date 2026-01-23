# file = open('example.txt', 'r')
# for line in file:
#     # print(line)
#     print(repr(line))

# file.close()
# content = file.readline()
# content2 = file.readline()
# file.close()

# print(repr(content))
# print(repr(content2))

# print(str(content))

# print(content)

# file = open('output.txt', 'w')

# file.write('Hello, world!\n')

# lines = ['First line\n', 'Second line\n']
# file.writelines(lines)

# file.close()

# file = open('output.txt', 'a')
# file.write('Third line!\n')
# file.write('Last line!\n')
# file.close()

# with open('example.txt', 'r') as file:
#     for line in file:
#         print(repr(line))

try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist')