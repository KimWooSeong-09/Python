# 파일에 내용 추가
f = open("data_2.txt", "a")

for i in range(11, 22):
    f.write(f'{i}번째 줄 입니다.\n')

f.close()
print("정상 종료")