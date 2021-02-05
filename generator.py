# #           ............................................. 1 ..............................................
#
# def generator_function(num):
#     for i in range(num):
#         yield i*2
#
# g = generator_function(1000)
#
# # next(g)
# # next(g)
# # print(next(g))
#
# for value in g:
#     print(value)


#     ........................................... Exercise(fibonacci) .......................................

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for v in fib(10000):
    print(v)
    print(type(v))
