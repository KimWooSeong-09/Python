# III. 들여쓰기(Indentation)

Python은 들여쓰기로 코드 블록을 구분합니다. 일관된 공백 사용이 필수입니다.

- **공백 4칸** 권장 (PEP8)
- **Tab 대신 Space** 사용 권장

## 예시

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i}는 짝수")
    else:
        print(f"{i}는 홀수")
```

잘못된 들여쓰기는 `IndentationError`를 발생시킵니다.