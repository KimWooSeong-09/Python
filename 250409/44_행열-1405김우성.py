# 44-1
rows = int(input("행 수: "))
cols = int(input("열 수: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(i * j, end=" ")
    print()

# 44-2
rows = int(input("행 수 : "))
cols = int(input("열 수 : "))

num = 1  

for i in range(rows):
    for j in range(cols):
        if j == 0:
            print(f"{num}", end="")
        else:
            print(f" {num}", end="")
        num += 1
    print()
