# def add(x, y):
#     return X + y
# print(add(3, 5))
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
result = int(input("Enter number"))
result = fibonacci_recursive(result)
print(result)    
