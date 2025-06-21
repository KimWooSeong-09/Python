for i in range(1, 7):
    for j in range(1, 7):
        print(f'({i}, {j})', end=" ")
    print()

print()
print("-" * 40)
print()

for i in range(1, 7):
    for j in range(1, 7):
        print(f'({j}, {i})', end=" ")
    print()


print()
print("-" * 40)
print()


for i in range(1, 7):
    for j in range(1, 7):
        if i == j:
            print("       ", end="")
            continue
        else:
            print(f'({i}, {j})', end=" ")
    print()