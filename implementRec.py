def f(t,a,b):
    if (b == 0):
        return t
    if (b%2 == 0):
        return f(t, a*a, b/2)
    else:
        return f(t*a, a, b-1)
print(f(1,2,3))
