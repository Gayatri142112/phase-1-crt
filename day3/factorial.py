#write a python program to print factorial of a given number
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print(factorial(n))
