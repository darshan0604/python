# username = "Darshan"

# def test():
#     # username = "hello"
#     print(username)
    
# test()

# x = 99

# def func(y):
#     z = x + y
#     return z

# result = func(1)
# print(result)

# def func2():
#     global x
#     x = 10

# func2()
# print(x)
x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)        
#     return f2
 
# myResult = f1()

# myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

# def chaicoder(2):
#     def actual(x):
#         return x ** 2
#     return actual

f = chaicoder(2)
# g = chaicoder(3)

print(f)
