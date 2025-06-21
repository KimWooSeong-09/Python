f = open("data_1.txt", "w")

f.write("안녕하세요!")

content = input("입력 : ")
f.write(content)

f.close()