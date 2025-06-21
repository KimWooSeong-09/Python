import random as r

def genPass():
    chr = "abcdefghijklmnopqrstuvwxyz0123456789"
    passwd = ""
    for i in range(8):
        passwd += r.choice(chr)
    return passwd

# Main
for i in range(3):
    result = genPass()
    print(f'암호 {i + 1} : \033[31m {result} \033[31m')
