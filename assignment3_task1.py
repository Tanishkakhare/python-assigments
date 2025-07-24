 # find the factorial of a given number

def factorial(n):
     if n < 2:
         return 1
     else:
         return n * factorial(n-1)

n = int(input("enter your number :"))
result = factorial(n)
print("Factorial of",n,"is :",result)
