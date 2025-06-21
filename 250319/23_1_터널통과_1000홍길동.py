car_height = 170
ternul_first, ternul_second, ternul_third = map(int, input("터널 높이 입력 :").split())
min_ternul = min(ternul_first, ternul_second, ternul_third)
if min_ternul <= car_height:
    print("crash")
else:
    print("pass")