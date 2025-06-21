birth, gender = map(int, input().split("."))

birth_year = (birth // 10000)

if gender in [1, 2]:  
    birth_year += 1900
else:  
    birth_year += 2000

age = 2025 - birth_year + 1

gender1 = "남성" if gender in [1, 3] else "여성"

print(f"현재 나이 {age}살 {gender1}입니다.")
