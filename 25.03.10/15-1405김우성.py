stu1 = {'학반': 105, '번호': 20, '이름': '홍길동'}

# 딕셔너리에서 키를 사용하여 값 접근
print(stu1['학반'])  # 105
print(stu1['번호'])  # 20
print(stu1['이름'])  # 홍길동

# get() 메서드를 사용하여 키에 해당하는 값 가져오기
print(stu1.get('이름'))  # 홍길동

# 키가 존재하지 않으면 None 반환 (get() 메서드()
print(stu1.get('주소'))  # None

# 여기서 오류 발생: stu1['주소']는 존재하지 않는 키이므로 KeyError 발생
# print(stu1['주소'])  # 오류 발생: KeyError: '주소'

# 딕셔너리의 키 가져오기
print(stu1.keys())  # dict_keys(['학반', '번호', '이름'])

# 딕셔너리의 키를 리스트로 변환
print(list(stu1.keys()))  # ['학반', '번호', '이름']

# 딕셔너리의 값 가져오기 (메서드 호출 필요)
print(list(stu1.values()))  # dict_values([105, 20, '홍길동'])

# 키가 딕셔너리 안에 있는지 확인
print('이름' in stu1)  # True
print('주소' in stu1)  # False
