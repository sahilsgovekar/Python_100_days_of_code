#errors and exception
# Try Except Else Finally

# a = int(input())
# b = int(input())

# try:
#     res = a/b
# except ZeroDivisionError as error:
#     print(error)
#     print("anything cannot be divided by zero")
# else:
#     print(res)
# finally:
#     print("Code execution done")


#raising own exception
#using raise keyword

n = int(input("Enter your height : "))
if n > 10:
    raise ValueError("Human Height Cannot be of that range")


