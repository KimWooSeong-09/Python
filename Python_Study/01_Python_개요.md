# I. Python 개념

Python은 1991년 귀도 반 로섬(Guido van Rossum)이 발표한 고급 프로그래밍 언어로, 가독성과 생산성을 중요시합니다.

- **인터프리터 언어**: 코드 작성 후 즉시 실행 가능, 빠른 프로토타이핑 지원
- **동적 타이핑**: 변수 선언 시 타입 명시 불필요
- **자동 메모리 관리**: 가비지 컬렉션으로 메모리 해제 자동 처리
- **풍부한 표준 라이브러리**: `os`, `sys`, `re`, `json` 등
- **크로스 플랫폼**: Windows, macOS, Linux 지원

## 간단 예제

```python
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    for person in ["Alice", "Bob", "Charlie"]:
        greet(person)
```