import random as r
print(r.random())
print(r.uniform(10, 11))
print(r.randint(10, 100))
print(r.randrange(10, 100, 10))
a_list = list(range(1, 10))
print(r.choice(a_list))
print(r.choices(a_list, k=3))
print(r.sample(a_list, k=2))
teacher = ['마아람', '정다혜', '강진아', '이승호']
r.shuffle(teacher)
print(teacher)
