class TV:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self): 
        print(f'채널: {self.channel}, 볼륨: {self.volume}, ON?: {self.on}')

    def setChannel(self, newChannel): 
        self.channel = newChannel

    def getChannel(self):
        return self.channel

tvInfo = TV(9, 10, True)

tvInfo.show()
tvInfo.setChannel(11)
tvInfo.show()