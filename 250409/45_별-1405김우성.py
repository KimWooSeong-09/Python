#45-1

a = int(input("행 수 : "))

for i in range(1, a + 1):
    print("*" * i)


# 45-2
b = int(input("행 수 : "))

for i in range(b, 0, -1):
    print("*" * i)

# 45-3
c = int(input("행 수 : "))

for i in range(1, c + 1):
    print(" " * (c - i) + "*" * i)

# 45-4
d = int(input("행 수 : "))

for i in range(d, 0, -1):
    print(" " * (d - i) + "*" * i)

# 45-5

a = int(input("행 수: "))

for i in range(1, a+1):
    for j in range(a, 1, -1):
        print(" " * j + "*" * i)