#42-1

user_input = int(input("자연수 : "))

for i in range(1, user_input + 1):
    if user_input % i == 0:
        print(i)

#42-2

user_input = int(input("자연수 : "))

for i in range(user_input, 0, -1):
    if user_input % i == 0:
        print(i)

