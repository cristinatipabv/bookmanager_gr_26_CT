# var1 = True
# var2 = 0
#
# if var1:
#     var2 = 10
#     print ("hello")
#
#     if var2 == 10:
#         print("success")

#Process finished with exit code 1
#x = 1 / 0

#Process finished with exit code 0
# x = 1
# print(x)

# try / catch

try:
    print("starting to divide by zero")
    x = 1 / 0
    print(x)
    print("universe just blew up")

except ZeroDivisionError as ex1:
    print("exception occurred")
    print(ex1)

except ValueError as ex2:
    print(ex2)

except Exception as ex3:
    print(ex3)

except AttributeError as ex4:
    # because exception is caught earlier, we wan't get gere in this attributeerror exception
    print(ex4)

finally:
    print("Finally")

print("and everything continues as it was")
print("end of file")