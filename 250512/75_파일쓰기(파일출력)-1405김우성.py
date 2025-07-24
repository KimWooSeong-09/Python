# 내용 표준입력 바당 팔이렝 한 줄씩 쓰기
# 내용이 없으면 종료
f = open("data_3.txt", "w")

while True:
    content = input("내용 입력 : ")

    if content != "":
        f.write(content)

    else:
        break

f.close()
print("정상 종료")