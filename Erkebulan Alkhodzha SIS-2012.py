Erkebulan Alkhodzha SIS-2012
# 1. Write program to swap two numbers without third variable
# a = int(input('a='))
# b = int(input('b='))
#
# a, b = b, a
#
# print(f"a={a}\n"
#       f"b={b}")


# 2. Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.
# def long_burp(count):
#     print(f"Bu" + 'r' * count + 'p')
#
#
# long_burp(3)

# 3. Create a function that takes a string and removes vowels contained within it
# import re
# def remove_vowels(text):
#     newText = re.sub(r'[AEIOU]', '*', text, flags=re.IGNORECASE)
#     print(newText)
# 
#     
# remove_vowels("Apple")

# 1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.
#
# def say_hello_bye(text, number):
#     if number == 1:
#         print(f'Hello {text}')
#     elif number == 0:
#         print(f'Bye {text}')
#
#
# say_hello_bye('Erkebulan', 1)
# say_hello_bye('Erkebulan', 0)


# 2. Create a function that takes a string as an argument and returns a coded version of the string.
#
# def coded_string(text):
#     for x in range(0, len(text)):
#         if(text[x] == 'a'):
#             text[x].replace('o', '0')
#         elif(text[x] == 'a'):
#             text[x].replace('u', '1')
#         elif(text[x] == 'a'):
#             text[x].replace('e', '3')
#         elif(text[x] == 'a'):
#             text[x].replace('a', '4')
#         elif(text[x] == 'a'):
#             text[x].replace('s', '5')
#
#     print(text)
#
#
# coded_string('Bekadil')

# 3. Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

# def equal(a,b,c):
#     if a==b and a==c and b==c:
#         print(a+b+c)
#     elif a==b and a!=c and b!=c:
#         print(a+b)
#     elif a==c and a!=b and b!=c:
#         print(a+c)
#     elif b==c and b!=a and c!=a:
#         print(c+b)
#     else:
#         print(0)
# 
# equal(1,1,2)