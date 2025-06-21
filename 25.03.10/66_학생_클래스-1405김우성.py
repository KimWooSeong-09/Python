class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕! 나는 고등학생 {self.age}학년 {self.name}이라고 해!')

s1 = Student("지민", 2)
s1.introduce()

s2 = Student("태형", 1)
s2.introduce()




