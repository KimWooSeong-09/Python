def fun_s(n):
    if n < 2:
        return 1
    else:
        return n + fun_s(n - 1)

# Main
print(fun_s(1))
print(fun_s(10))
a = int(input("자연수 : "))
print(fun_s(a))

def fun_f(n):
    if n < 2:
        return 1
    else:
        return n * fun_f(n - 1)

# Main
print(fun_f(1))
print(fun_f(10))
b = int(input("자연수 : "))
print(fun_f(b))