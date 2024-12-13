try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Don't divide by zero")
except SyntaxError:
    print("Use commma between two numbers")
except NameError:
    print("Only use numbers")
except TypeError:
    print("Don't use any text")
finally:
    print("Your code is correct")