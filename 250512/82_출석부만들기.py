# 이름 여러 개 입력받아 attendance.txt에 한 줄씩 저장
with open("attendance.txt", "w") as f:
    for i in range(5):
        name = input(f"{i + 1}번 : ")
        f.write(f'{i + 1} 번 : {name}\n')