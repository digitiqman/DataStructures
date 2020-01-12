"""
the fibonacci sequence
"""

# recursively
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

# iteratively
def Fib(n):
    f = (n+1)*[0]
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]
