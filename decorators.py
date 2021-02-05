
#                                 ..............................1st...........................

# def hello():
#     print('helloooooooooooooooo')
#
# greet = hello
# print(greet())
#
#  # del hello
#  # print(hello())     #    name 'hello' is not defined

# #.......

# def hello(func):
#     func()
#
# def greet():
#     print('still here!')
#
# a = hello(greet)
# print(a)

#                               ..............................2nd...........................
# higher order function(hof).......
# A function is called Higher Order Function if it contains other functions as a parameter or
# returns a function as an output i.e, the functions that operate with another function
# are known as Higher order Function

# def greet(func):
#     func()
#
# def greet2():
#     def func():
#         return 5
#     return func

#                                          ..............................3rd(decorator basic)...........................
#     decorator-> they are functions which modify the functionality of other functions. They help to make our code shorter and more Pythonic
# def my_decorator(func):
#     def wrap_func():
#         print('......')
#         func()
#         print('......')
#     return wrap_func
#
# @my_decorator
# def hello():
#     print('hellloooo')
#
# hello()
# # same way 1
# # hello2 = my_decorator(hello)
# # hello2()
# # same way 2
# # my_decorator(hello)()

#                                              ..............................4th.............................
# def my_decorator(func):
#     def wrap_func(x):
#         print('......')
#         func(x)
#         print('......')
#     return wrap_func
#
# @my_decorator
# def hello(greeting):
#     print(greeting)
#
# hello('hellooo')
# ........
# def my_decorator(func):
#     def wrap_func(*args,**kwargs):      # *args-> all positioning arguments    *kwargs -> all keyword arguments
#         print('......')
#         func(*args,**kwargs)
#         print('......')
#     return wrap_func
#
# @my_decorator
# def hello(greeting,emoji,name):
#     print(greeting,emoji,name)
#
# hello('hellooo',':(', 'Akash')

#                                  ..............................5th(practical example -> Execution time).............................
# from time import time
#
#
# from time import time
#
#
# def performance(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time()
#         result = fn(*args,**kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper()
#
# @performance
# def long_time():
#     for i in range(100000):
#        i * 5
#
# long_time()

#                      ..............................Exercise.............................
# user1 = {
#     'name':'Akash',
#     'valid': False
# }
#
# def authenticated(fn):
#     def wrapper(*args,**kwargs):
#         if args[0]['valid']:
#             return fn(*args,**kwargs)
#     return wrapper
#
# @authenticated
# def message_friends(user):
#     print('massage has been sent ..')
#
# message_friends(user1)
# import urllib

#                   ..........................send url by python...............................
# import urllib.request
#
# url = "http://aaHR0cHM6Ly9mb3Jtcy5nbGUvWU5ZXQ0d2NRWHVLNnNwdjU="
#
#
# status_code = urllib.request.urlopen(url).getcode()
#
# website_is_up = status_code == 200
#
#
# print(website_is_up)

import urllib
import urllib.request , urllib.error
from urllib.request import urlopen

filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       # print(line.strip())
       # print("Line {}: {}".format(cnt, line.strip()))
       print(f"Line {cnt} {line.strip()}")
       # url = line.strip()
       # print(type(url))
       #
       # status_code = urllib.request.urlopen(url).getcode()
       # print(website_is_up)
       line = fp.readline()
       cnt += 1



