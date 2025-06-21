# 38-1
user_input = int(input("어디까지 출력할까요? : "))

for i in range(user_input):
    print(i + 1)

# 38-2
user_input = int(input("어디부터 출력할까요? : "))

for i in range(user_input, -1, -1):
    print(i)

# 38-3
user_input = int(input("몇 단? : "))

print("=== 8단 ===")
for i in range(9):
    print(f'{user_input} * {i + 1} = {user_input * (i + 1)}')