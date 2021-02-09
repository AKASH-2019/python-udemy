
# #  ............................... 1 ....................................
# my_file = open('file1.txt')
# print(my_file.read())
# print(my_file.read())    #    curser present at the end of file so blank output
# print(my_file.read())    #    curser present at the end of file so blank output
# # ..............
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
#
# # ..................
# print(my_file.readline())
#
# print(my_file.readlines())


# my_file.close()

# #  ............................... 2 ....................................
# with open('file2.txt', mode='r+') as my_file:
#     print(my_file.write('Assalamualaikum..'))
# #..........
# with open('file2.txt', mode='r+') as my_file:
#     print(my_file.write(':)'))
# #..........
# with open('file2.txt', mode='a') as my_file:
#     print(my_file.write(':)'))
# #..........
# with open('file2.txt', mode='w') as my_file:
#     print(my_file.write(':)'))
# #.......... file does not exist
# with open('sad.txt', mode='w') as my_file:
#     print(my_file.write(':('))

# #  ............................... 3 ....................................
# file is exist in another folder....

# with open('folder_name(path)/sad.txt', mode='w') as my_file:
#     print(my_file.write(':('))

# #  ............................... 4 ....................................
# error....
# # ............
# try:
#    with open('test.txt', mode='r') as my_file:          # folder/test.txt
#         print(my_file.read())
# except FileNotFoundError as err:
#     print('file does not exist')
#     raise err
# # .............
# try:
#    with open('test.txt', mode='x') as my_file:          # file/test.txt
#         print(my_file.read())
# except IOError as err:
#     print('IO error')
#     raise err

# #  ............................... 5 ....................................
from translate import Translator

translator= Translator(to_lang="zh")
try:
    with open('file5.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('file-japanis.txt', mode='w') as my_file2:
           my_file2.write(translation)
except FileNotFoundError as err:
    print('FIle not found')