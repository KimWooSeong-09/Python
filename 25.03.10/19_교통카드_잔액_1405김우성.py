# 방법 1 
fee = int(input("정해진 요금을 입력해주세요 : "))
card = int(input("카드 잔액 : "))

if fee <= card:
    print("탑승가능")
else:
    print("탑승 불가능")

# 방법 2

fee = int(input("정해진 요금을 입력해주세요 : "))
card = int(input("카드 잔액 : "))

if card < fee:
    print("탑승불가능")
else:
    print("탑승가능")