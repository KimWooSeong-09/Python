fruit_weight = int(input("과일 무게(g) : "))

if 300 <= fruit_weight < 375:
    print('"특"')
elif 250 <= fruit_weight < 300:
    print('"상"')
elif 210 <= fruit_weight < 250:
    print('"보통"')
else:
    print('"판정 불가"')