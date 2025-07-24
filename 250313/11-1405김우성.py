programing = ['홍길동', '일지매']
print(f'현재 프로그래밍 수강 신청자는 {programing}입니다.')
a = input("추가 신청할 학생 이름 : ")
programing.append(a) # 신청 학생 입력
print(f'현재 이 과목의 최종 신청자는 {programing}입니다.')
b = input("철회할 학생 이름 : ") # 철회 학생 입력
programing.remove(b)
print(f'{b} 학생의 수강 철회가 완료되었습니다.')
print(f'현재 이 과목의 최종 신청자는 {programing}입니다.')

programing = ['일지매', '전우치']

a = input("변경 전 이름 : ")
b = input("변경 후 이름 : ")

if a in programing:
    programing[programing.index(a)] = b
    print(f'요청하신 대로 {a}을(를) {b}로 변경하였습니다.')
else:
    print(f'"{a}"은(는) 목록에 없습니다.')

print(f'변경된 리스트는 {programing}입니다.')
