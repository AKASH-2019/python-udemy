#
# # int float ...........................................
#
# print(2+4)
# print(type(2+4))
# print(type(2+40))
# print(type(2+4.0))
# print(type(2.22+4.88))
#
# # power (n ** p) .........................................
# print(2 ** 2)
# print(2 ** 3)
# print(5 ** 3)
#
# # rounded divisible value ( // ) ..........................
# print(3 // 4)
# print(5 // 4)
# print(15 // 4)
# print(25 // 4)
# print(type(15 // 4))
#
# # Remainder ...................................
# print(3 % 4)
# print(15 % 4)
# print(25 % 4)
#
# # math function ( also from google ) ................................
# print(round(3.1))
# print(round(3.9))
# print(abs(-3.1))
# print(abs(-3.1+2))
#
# # binary ...........................................
# print(bin(5))
# print(int('0b101', 2))
#
# # augmented assignment operator ...................................
# value = 5
# value +=3   # += this call aug...
# value -=2
# value *=2
# print(value)
#
#                           ..................................string..............................................
#
# # string ............................................................................
# first_name = 'Munazer Montasir'
# last_name = "Akash"
# full_name = first_name + ' ' + last_name
# print(full_name)
#          # for long string use ''' string '''
# long_str = '''
# WOW
# 0 0
# ---
# '''
# print(long_str)
#
# # escape sequence .............................................
#       #   ( 's "text" tab-> \t newline-> \n )  in string whatever come after \ this it recognize as string
# weather = 'it\'s \"kind of\" sunny'
# print(weather)
#
# weather = '\t it\'s \"kind of\" sunny \n hope you have a good day!'
# print(weather)
#
# # formatted string .....................................................................
# name = 'Akash'
# age = 56
#
# print('hi ' + name + '. you are ' + str(age) + ' years old')
#
#     # for formatting string a new use -> f beginning the string..
# print(f'hi {name}. you are {age}  years old')  # for python 3
#
# print('hi {}. you are {}  years old'.format(name,age))   # .format in python 2
# print('hi {1}. you are {0}  years old'.format(name,age))
#
# print('hi {new_name}. you are {age}  years old'.format(new_name='Shihab',age=56))
#
# # string indexes ......................................................................
# text = 'munazer'
# print(text[1:6])
# print(text[0:6:2])     # text[start:stop: step over]
# print(text[::2])
# print(text[-3])
#
# print(text[::-1])  # reverse string
# print(text[::-2])
#
# # string built in function ...................................................................
# text = 'to be or not to be'
# length = len(text)
# print(text[1:len(text)])
#
# print(text.upper())   # all char. convert to upp..
# print(text.capitalize())  # only first letter convert to upp..
# print(text.find('be'))     # for find
# print(text.replace('be', 'me'))  # for replace char
# print(text.replace('be', 'me', 1))
# print(text)    # python string Immutability -> not change
#
#     Return the string without any whitespace at the beginning or the end.
# txt = " Hello World "
# print(txt.strip())


# #                    ..................................booleans..............................................
# flag = True
# flag = False
# print(bool(1))    # output -> True
# print(bool('True'))
# print(bool(0))
#
# # type conversion  ...............................................................
# print(type(str(100)))
# print(type(int(str(100))))
#
# birth_year = input('What year were you born?')
# age = 2020 - int(birth_year)
# print(f'your age is: {age}')
#
# # password checker ...................................................................
# username = input('what is your username?')
# password = input('what is your password?')
# password_length = len(password)
# hidden_password = ('*' * password_length)
# print(f'{username}, your password {hidden_password} is {password_length} letter long')
#
#                         ..................................list..............................................
#
# # list slicing ..........................................................................................
# amazon_cart = [
#     'notebooks',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]
# print(amazon_cart)
# print(amazon_cart[1::2])
# amazon_cart[0]='laptop'
# print(amazon_cart)    # list is mutable
#
# new_cart = amazon_cart[:]    # slicing.....
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)  # both new_cart and amazon_cart are changed to gum...
# print('this is difference from above')
# new_cart = amazon_cart    # both share same memory
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)  # both new_cart and amazon_cart are changed to gum...

# # Matrix .........................................................................................
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[2][1])

# list method ........................................................................................

# # adding method -> append(), insert(), extend([])....
# basket = [1,2,3,4,5]
# print(len(basket))   # length of list
#  # new_list =  basket.append(100)  # new_list -> none
# basket.append(100)     # adding value at the end of the list
# new_list = basket
# print(new_list)
#
# basket.insert(3,1000)   # adding value at any specific position
# print(basket)
#
# basket.extend([1005, 1010])   # adding more than 1 value in list
# print(basket)
#
# # remove .....
# basket.pop()        # remove the last element of the list
# print(basket)
# basket.pop(2)        # remove the specific index element of the list
# print(basket)
# pop_value = basket.pop(3)        # remove the specific index element of the list and assign in pop_value
# print(pop_value)
# basket.remove(100)        # remove the specific value of the list
# print(basket)
# basket.clear()       # remove all the element list
# print(basket)

# # index ......
# basket = ['a','b','c','d','e','d']
# index = basket.index('d')
# print(f'the index of d is: {index} ')
# # print(basket.index('d',0,3))       # index('char',start,end)
# print('d' in basket)  # output True
# print('x' in basket)  # output False
# print('ami' in 'i am akash')
# print('am' in 'i am akash')
#
# print(basket.count('d'))    # count
#
# print(sorted(basket))  # sort the list  ; produce new list. original is same as before
# print(basket)
# new_basket = basket.copy()
# new_basket.sort()
# print(new_basket)
# print(basket)
# basket.sort()  # sort the list
# print(basket)

# # dif btn sort() and sorted()  ......
# basket = ['z','a','b','c','d','e','d']
# sorted(basket)           # sort the list  ; produce new list. original is same as before
# basket.reverse()
# print(basket)
#
# basket.sort()           # sort the original list
# basket.reverse()
# print(basket)

# # dif btn reverse and [::-1] ....
# basket = ['z','a','b','c','d','e','d']
# print(basket[::-1])  # reverse the list with new list
# print(basket)
#
# basket.reverse()     # sort the original list

# # print specific range
# print(range(1,100))    # -> range(1, 100)
# print(list(range(1,100)))     # -> 1....99
# print(list(range(100)))     # -> 0....99

# # string  join  with list......
# sentence = '!'
# sentence.join(['hi','my','name','is','Akash'])  # !
# print(sentence)
# new_sen = sentence.join(['hi','my','name','is','Akash'])   # hi!my!name!is!Akash
# print(new_sen)
#
# sentence = ' '
# new_sen = sentence.join(['hi','my','name','is','Akash'])   # hi my name is Akash
# print(new_sen)

# # list unpacking...........
# a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# #  ................................................. None(absence of value) ................................................
# weapons = None  # same as NULL value of c/c++
# print(weapons)
#
#                            ..................................dictionary(map)..............................................
#                            dictionary -> data type and also data structure       -> {key:value,key:value}
#
# dictionary = {
#     'a': 1,
#     'b': 2
#
#     # 123 : [1, 2 , 3],
#     # [100] : 1   # key dose not contain list (key imutable  (not change)) but contain tuple
#     # (1,2) : 5
#     # 123 : 'hello'  # for key 123 output-> hello ; it is override on [1, 2, 3] ;
#     # True : 'ddd'    # valid ;  dictionary[True] -> ddd
# }
# print('a')
# print(dictionary)
#       #  with list and diff value
# dictionary = {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
# }
# print('a')
# print(dictionary['a'][1])
# print(dictionary)
#
# my_list = [
#     {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
#     },
#     {
#     'a': [4,8,3],
#     'b': 'hello!!',
#     'x': True
#     }
# ]
# print(my_list[0]['a'][2])
# print(my_list[1]['a'][1])

# # dictionary method 1...........................
# dictionary = {
#     'basket': [1,2,3],
#     'greet': 'hello',
#     # 'age': 56
# }
# # print(dictionary['age']) # age key word does not exist
# print(dictionary.get('age'))   # None
# # another way to define dic. but not common
# user = dict(age = 56)
# print(user)
# dictionary method 2...........................
# user = {
#     'basket': [1,2,3],
#     'greet': 'hello',
#     # 'age': 56
# }
# print('basket' in user)           # True    ; default user means key
# print('size' in user)             # False
# print('size' in user.keys())      # False
#
# print('hello' in user.values())      # True
#
# print(user.items())   # print whole dictionary
#
# # user.clear()   print(user)-> None
# user2 = user.copy()  #
#
# # print(user.pop('age'))  # -> 20
# # print(user)   # age item deleted
#
# # print(user.popitme())  # randomly delete 1 item
# # print(user)   # missing 1 item
#
# print(user.update({'age' : 20}))
# print(user)
# print(user.update({'point' : 35}))   # add this new item
# print(user)

#                         ..................................tuple(like list but imutable)..............................................
#                        if not change data in list then use tuple, efficient (+ net)
# my_tuple = (1, 2, 3,4,5)
# # my_tuple[1]='z'      # tuple imutable ...
# print(my_tuple[1])
# print(5 in my_tuple)  # True / False
# dictionary = {
#     # [100] : 1   # key dose not contain list (key imutable  (not change)) but contain tuple
#      (1,2) : 5
# }
# print(dictionary[(1,2)])
#
# new_tuple = my_tuple[1:2]
# print(new_tuple)
# new_tuple = my_tuple[1:4]
# print(new_tuple)
# x,y,z,*other = (1, 2, 3,4,5)
# print(z)
# print(other)

# # tuple method (only 2 method).........
# my_tuple = (1, 2, 3,4,5,4)
# print(my_tuple.count(4))  # 2
# print(my_tuple.count(3))  # 1
#
# print(my_tuple.index(4))  # 3
# print(len(my_tuple))

#                               ......................................sets..............................................
#                               unordered collection of unique item (no duplicate value)
# my_set = {1,6,2,3,4,5,5}
# print(my_set)    #    {1, 2, 3, 4, 5, 6}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# # print(my_set[1])      # error -> does not support indexing
# print(1 in my_set)      # True
# print(len(my_set))
#
# new_set = my_set.copy()
# my_set.clear()
# print(new_set)
# print(my_set)
#
# my_list = [1,6,2,3,4,5,5]      # how only take the unique value from this array/list?
# print(set(my_list))

# set method 2..............
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# difference() -> compare with 2 set              ( difference() not modify but difference_update() modify)
# print(my_set.difference(your_set)) # {1, 2, 3}

# discard() -> remove the element
# print(my_set.discard(5))   # none
# print(my_set)       # remove 5

# difference_update() -> remove the same element of 1st set          ( difference() not modify but difference_update() modify )
# print(my_set.difference_update(your_set))
# print(my_set)          #       {1, 2, 3}

# intersection()    -> show the same element
# print(my_set.intersection(your_set))
# print(my_set & your_set)    # this is also union()

# isdisjoint()   -> overlap(False) or not(True)
# print(my_set.isdisjoint(your_set))  # -> false 4 5 are same both

# issubset()
# print(my_set.issubset(your_set))        #       False
#
# my_set = {4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.issubset(your_set))       #          True
#
# # issuperset()
# my_set = {4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.issuperset(your_set))   # my_set does not contain all value of your_set  so-> False
# print(your_set.issuperset(my_set))   # your_set  contain all value of my_set  so-> True

# union()   -> unite the both set without duplicate
# print(my_set.union(your_set))
# print(my_set | your_set)    # this is also union()

