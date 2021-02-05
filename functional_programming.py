# #               .................................... map ..................................
#
# my_list = [1,2,3]
#
# def multiply_2(item):
#     return item*2
#
# print(list(map(multiply_2, my_list)))
# print(my_list)          #  same as before -> immutable
#
# my_list = [1,2,3,4]
#
# def chk_odd_even(item):
#     return item % 2==0
#
# ans = (list(map(chk_odd_even, my_list)))
# print(ans)
# print(my_list)

#
# #  exercise: capitalize the username........................
#
# username = ['akash', 'chyon', 'arif', 'shihab', 'forhad', 'shafayet']
#
# def cap(username):
#     return username.capitalize()
#
# username = (list(map(cap, username)))
# print(username)

#               .................................... filter ..................................

# my_list = [1,2,3,4]
#
# def only_odd(item):
#     return item % 2 !=0
#
# ans = (list(filter(only_odd, my_list)))
# print(ans)
# print(my_list)

# #  exercise -> username starting with A .............................
#
# username = ['akash', 'chyon', 'arif', 'shihab', 'forhad', 'shafayet']
#
# def cap(username):
#     return username.capitalize()
#
# username = (list(map(cap, username)))
#
# def start_with_A(username):
#     return username[0] == 'A'
#
# username_A = (list(filter(start_with_A, username)))
# print(username_A)

# #              ........................................ zip ................................................
#
# username_clm = ['akash', 'chyon', 'arif', 'shihab', 'forhad', 'shafayet']
# phone_clm = ['123', '222', '333','444', '555', '666']
# address_clm = ('a1', 'b1', 'c1', 'd1', 'e1', 'f1')
#
# new_list = list(zip(username_clm,phone_clm,address_clm))
# print(new_list)
# print(new_list[0][2])

# #              ........................................ reduce ................................................
from functools import reduce
# my_list = [3,2,5]
#
# def accumulator(acc,item):         #  accumulator sum....
#     print(acc, item)
#     return acc + item
#
# # initial with 0
# print(reduce(accumulator,my_list,0))
#
# # initial with 10
# print(reduce(accumulator,my_list,10))

# #              ........................................ lambda ................................................
# my_list = [3,4,5]
#
# # map
# print(f'multiply the my_list by2 : {list(map(lambda item: item*2, my_list))}')
#
# # filter
# print(f'odd only : {list(filter(lambda item: item % 2 != 0, my_list))}')
#
# # reduce
# print(f'accumulator : {reduce(lambda acc, item: acc + item, my_list)}')


