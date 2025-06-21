# 47(list)
user_input = input("영문자열 입력 : ")
print("#" * 20)

vow_list = ['a', 'e', 'i', 'o', 'u']
vow_c = 0
con_c = 0

for char in user_input:
    if char.isalpha(): 
        if char.lower() in vow_list:
            vow_c += 1
        else:
            con_c += 1

print(f'모음 개수 : {vow_c} ㅣ 자음 개수 : {con_c}')


# 47(string)

user_input = input("영문자열 입력 : ")
print("#" * 20)

vow_list = 'aeiou'
vow_c = 0
con_c = 0

for char in user_input:
    if char.isalpha():
        if char.lower() in vow_list:
            vow_c += 1
        else:
            con_c += 1

print(f'모음 개수 : {vow_c} ㅣ 자음 개수 : {con_c}')


