# 이밎 모듈 호출
from PIL import Image

# 이미지 열기
img = Image.open("sample.jpeg")
img.show()

# 이미지 정보 확인
print("이미지 크기 : ", img.size)
print("이미지 형식 : ", img.format)
print("이미지 모드 : ", img.mode)

