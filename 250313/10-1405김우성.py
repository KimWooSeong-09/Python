data = [30, 10, 20]
print(f'전체 리스트 : {data}')
print(f'리스트 데이터 개수: {len(data)}')
data.append(40)
print(f'40 추가 후의 리스트: {data}')
last = data.pop()
print(f'리스트 마지막 데이터: {last}')
print(f'추출 후 리스트 : {data}')
data.sort()
print(f'오름차순 정렬 : {data}')
data.reverse()
print(f'리스트 역순 : {data}')
a = data.index(20)
print(f'데이터 20의 위치 : {a}')
data.insert(1, 222)
print(f'index 2 위치에 222 삽입 후의 리스트 : {data}')
data.remove(222)
print(f'222 삭제 후의 리스트 : {data}')
data2 = [77, 88, 77]
data.extend(data2)
print(f'data2를 만들어서 data와 연결한 값 : {data}')
data.remove(10)
print(f'index 2 위치의 데이터 삭제 후 리스트 : {data}')
