def factorial(n):
    '''this function returns the factorial of a number'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial.__doc__)
print("Factorial of 1 is", factorial(1))
print("Factorial of 2 is", factorial(2))
print("Factorial of 3 is", factorial(3))
print("Factorial of 4 is", factorial(4))
print("Factorial of 5 is", factorial(5))
print("Factorial of 34 is", factorial(34))
