class remoteControl:

    def __init__(self, tv: str, room: str):
        self.tv = tv
        self.room = room
        self.channel = 0

    def forwardChannel(self):
        self.channel += 1
        print(f'Avançar canal: {self.channel}')

    def backwardChannel(self):
        self.channel -= 1
        print(f'Voltar Canal: {self.channel}')

    def chooseChannel(self, channel):
        print(f'Alterando canal para {channel}')
        self.channel = channel


livingRoomControl = remoteControl("Samsung", "Sala")
print(livingRoomControl.room, livingRoomControl.tv, livingRoomControl.tv)
livingRoomControl.chooseChannel(13)
livingRoomControl.forwardChannel()

