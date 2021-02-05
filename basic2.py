import emoji


#                         ........................................ truthy and falsy................................
# print(bool(5))             # truthy
# print(bool('hello'))       # truthy
# print(bool(0))             # falsy
# print(bool(''))            # falsy

#                         ........................................ Ternary .........................................
# is_friend = False
# can_message = 'message is allowed' if is_friend else 'message not allowed'
# print(can_message)

#                         ........................................ Logical operator .........................................
# print(4 > 5)
# print('a' < 'b')
# print(1 < 2 >= 3 < 4)
# print(1 < 2 < 3 < 4)
# print(4 == 5)
# print(1 != 0)
# print(not True)
# print(not (1 == 1))

# Exercise
# is_magician = False
# is_expert = True
#
# if is_magician and is_expert:
#     print('You are a master magician')
# elif is_magician and not is_expert:
#     print('at least you are getting there')
# elif not is_magician:
#     print("You need magic powers")

#                              ........................................ is vs == .........................................
#  The Equality operator (==) compares the values of both the operands and checks for value equality.
#  Whereas the ‘is’ operator checks whether both the operands refer to the same object or not.(is same loc or not)
# print(True == 1)    # T
# print('1' == 1)     # F (not in same loc)
# print([] == 1)      # F (not in same loc)
# print(10 == 10.0)   # T
# print([] == [])     # T
#
# print(True is 1)     # F (not in same loc)
# print('1' is 1)      # F (not in same loc)
# print(10 is 10.0)    # F (not in same loc)
# print([] is [])      # F (not in same loc)
#
# print(1 is 1)      # T
# print('1' is '1')  # T
# print(10 is 10.0)  # F (not in same loc)
# print([] is [])    # F (not in same loc)

# a = [1,2,3]
# b = [1,2,3]
# print(a is b)   # F (not in same loc)
# print(a == b)   # T

#                                 ........................................ loops .........................................
# for item in "zero to mastery":
#     print(item)
# for item in [1,2,3,4]:           # list
#     print(item)
# for item in {1,2,3,4}:           # set
#     print(item)
# for item in (1,2,3,4):           # tuple
#     print(item)

# for item in (1,2,3,4):           # tuple
#     for x in ['a','b','c']:
#         print(item,x)

#                         ........................................ loops(iterable) .........................................
# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }
#
# for k,v in user.items():
#     print(k,v)
#
# for item in user.values():
#     print(item)
#
# for item in user.keys():
#     print(item)

# exercise
# my_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for item in my_list:
#     sum += item
#     print(item)
# print(f'sum of the all array element is {sum}')

#                               ........................................ loops(range) .........................................
# for _ in range(0,10):
#     print(_)
# print('\n')
# for _ in range(0,10,2):
#     print(_)
# print('\n')
# for _ in range(10,0,-2):
#     print(_)
#
# # print(list(range(0,10)))
# for _ in range(2):
#     print(list(range(0, 10)))

#                     ........................................ loops(enumerate-> print with index) .........................................
# for i,v in enumerate('Hellooo'):
#     print(i,v)
# for i,v in enumerate([1,2,3]):    # same as      (1,2,3)     {1,2,3}
#     print(i,v)
# # exercise -> print the index of 50
# for i,v in enumerate(list(range(100))):
#     if i == 50:
#         print(f'the index of 50: {i}')
#         break

#                 ........................................ loops(while and else) .........................................
# i = 0
# while i > 50:
#     print(i)
# else:
#     print('done with all the work')
#
# # dif
# i = 0
# while i > 50:
#     print(i)
#     break
# else:           #    if break state. execute then the else sta. is not exe..
#     print('done with all the work')


# while True:
#     response = input('say something: ')
#     if response == 'bye':
#         break

# continue
#
# pass

# #  Exercise
# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]
#
# for image in picture:
#     for pixel in image:
#         if pixel==1:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()

# #     Check duplicates in a list........
# some_list = ['a','b','c','b','d','m','n','n']
# duplicate = []
# for value in some_list:
#     if some_list.count(value)>1:
#         if value not in duplicate:
#             duplicate.append(value)
#
# print(duplicate)

#    ..........................................function()....................................
# def say_hi():
#     print('Assalamualaikum....')
#
# say_hi()
# print(say_hi)             #        location

# print(emoji.emojize('Python is :red_heart:',variant="emoji_type"))
#
# def say_hi(name, emoji):
#     print(f'Assalamualaikum....{name} {emoji}')
#
# say_hi('Akash', emoji.emojize(':red_heart:',variant="emoji_type"))
# print(say_hi)             #        location

# def sum(a,b):
#     def another(a,b):
#         return a+b
#     return another
#
# total = sum(10, 20)
# print(total(10, 5))

# def sum(a,b):
#     def another(a,b):
#         return a+b
#     return another(a,b)
#
# total = sum(10, 20)
# print(total)

#     ................method vs function...........................

# function
# list()
# max()
# print()
# input()
#
# def sum():
#     return sum
# sum()

# method (using . )
# str = 'assalamualaikum..'.capitalize()
# print(str)

#                               ................docstring..........................
# def test(a):
#     '''
#      info: this fun test and print parm a
#     '''
#     return a;
#
# test()
# print(test.__doc__)

# #                            ....................clean code..........................
# def even_or_odd(num):
#     return num % 2 == 0
# print(even_or_odd(50),end=" ")
# print(even_or_odd(51))

#                            ....................*args and *kwargs..........................
# #   *args -> accept any positional argument            arg -> accept 1 arg
# def sum_fun(*args):
#     print(args)         # (1, 2, 3,4)   tuple
#     return sum(args)
#
# def min_fun(*args):
#     return min(args)
#
# print(sum_fun(1,2,3,4))
# print(min_fun(5,2,3,4))

#   **kwargs -> accept any positional argument
# def sum_fun(*args,**kwargs):
#     print(args)         # (1, 2, 3,4)   tuple
#     print(kwargs)       # {'num1': 5, 'num2': 10}       dictionary
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return sum(args) +total
#
# print(sum_fun(1,2,3,4, num1=5, num2=10))

# # ordering of parameter in a function
# func(parm, *args, default_parm, **kwargs)
# func(name, *args, gre='hi', **kwargs)

#                  ...................................func_exercise.................................
# def highest_even(*args):
#     max_even = 0
#     for item in args:
#         if item % 2 ==0:
#             if max_even<item:
#                 max_even = item
#     return max_even
#
# print(highest_even(10,2,5,9,11))   # using tuple
#
# def highest_even(li):
#     even = []
#     for item in li:
#         if item % 2 ==0:
#             even.append(item)
#     return max(even)
#
# print(highest_even([10,2,5,9,11]))

x = complex(5)
print(x)












