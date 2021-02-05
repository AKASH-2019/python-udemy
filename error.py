

# #             ..............................................1..........................................
# while True:
#     try:
#         age = int(input('Please enter your age: '))
#         print(age/age)
#     except ValueError:
#         print('Enter a int number!!')
#     except ZeroDivisionError:
#         print('please enter a age higher than zero')
#     else:
#         print('Thank you')
#         break

#             ..............................................2..........................................

def sum(num1, num2):
    try:
       return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    finally:
        print('i am finally done')


print(sum(1,'2'))
print(sum(1,0))
print(sum(10,5))

#             ..............................................3 4..........................................


