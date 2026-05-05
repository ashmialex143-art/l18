try:
    num1,num2 = eval(input("enter two numbers,seperated by a coma:"))
    result = num1 / num2
    print("result is",result)

except ZeroDivisionError:
    print("division by zero is error !!")

except SyntaxError:
    print("coma is missing.")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")