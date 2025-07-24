class TV:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def setChannel(self, channel):
        self.channel = channel

    def setVolume(self, volume):
        self.volume = volume

    def setOn(self, on):
        self.on = on

    def show(self):
        print(f'현재 채널은 {self.channel}번이고, 볼륨은 {self.volume}이며 티비 상태는 {"켜짐" if self.on else "꺼짐"}입니다.')


my_tv = TV(0, 0, True)

while True:
    my_tv.show()
    user_input = input("어느 것을 바꾸시겠습니까?(1.채널 2.볼륨 3.on/off 4.그만두기): ")
    
    if user_input == "1":
        channel = int(input("몇번 채널로 바꾸시겠습니까? : "))
        my_tv.setChannel(channel)
    elif user_input == "2":
        volume = int(input("볼륨을 설정해주세요 : "))
        my_tv.setVolume(volume)
    elif user_input == "3":
        on_off = int(input("(1. 켜기 2. 끄기) : "))
        if on_off == 1:
            my_tv.setOn(True)
        elif on_off == 2:
            my_tv.setOn(False)
        else:
            print("잘못된 입력입니다.")
    elif user_input == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 보기 중으로 설정해주세요.")
