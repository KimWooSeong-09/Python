hap_list = []
avg_list = []
count = 0

while True:
    score = float(input("점수 입력 (0 이하 입력 시 종료): "))
    if score > 0:
        hap_list.append(score)
        avg_list.append(score)
        print(f'{score}이(가) 성공적으로 추가되었습니다!')
        count += 1
    else:
        break  # 0 이하 입력 시 루프 종료

if count > 0:
    hap = sum(hap_list)
    avg = round(sum(avg_list) / count, 1)
    print(f'최종 합 : {hap}, 최종 평균 : {avg}')
else:
    print("입력된 점수가 없습니다.")
