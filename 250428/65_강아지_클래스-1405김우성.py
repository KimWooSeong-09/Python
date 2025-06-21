class Dog:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind

    def bark(self):
        print(f'{self.name}이 왈왈 짖어요!')

    def sit(self):
        print(f'{self.kind}는 앉기도 잘해요')

    def dog_age(self):
        print(f'{self.name}은(는) {self.age}살 이에요.)')


# Main
my_dog = Dog("망고", 3, "푸들")
my_dog.bark()
my_dog.dog_age()

your_dog = Dog("당근", 5, "진도")
your_dog.sit()
your_dog.dog_age()
