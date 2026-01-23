# 1

# reciprocal_generator = (1/n for n in range(1,11))

# for num in reciprocal_generator:
#     print(num)

# 2

# def reciprocal_generator(n):
#     for i in range(1, n + 1):
#         yield 1 / i

# for num in reciprocal_generator(10):
#     print(num)

# 3

# strings = ['abe', 'bob', 'cody', 'doug', 'ethan']

# caps = (string.capitalize() for string in strings)

# print(tuple(caps))

# 4

# strings = ['abe', 'bob', 'cody', 'doug', 'ethan']

# def caps(string_list):
#     for string in string_list:
#         yield string.capitalize()

# print(tuple(caps(strings)))

# 5

# strings = ['abe', 'bobby', 'cornelius', 'doug', 'ethan']

# cap_greater_than_five = (string.capitalize() 
#                          for string in strings 
#                          if len(string) >= 5)

# print(set(cap_greater_than_five))

# 6

strings = ['abe', 'bobby', 'cornelius', 'doug', 'ethan']

def cap_less_than_five(string_list):
    for string in string_list:
        if len(string) < 5:
            yield string.capitalize()

print(set(cap_less_than_five(strings)))