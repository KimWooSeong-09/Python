height = float(input("키(cm)입력 : "))
weight = float(input("체중(kg)입력 : "))

if (130 <= height < 190) and (25<= weight < 100):
    print("이용 가능")
else:
    print("이용 불가능")