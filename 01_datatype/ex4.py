# 문자열
# "", ''

a = "python"
print(a, type(a))

# I'll be back
print("I'll be back")
print("I'll be back")

multiline = """
Life is short
You need python
"""  # 멀티라인으로 쓸 때는 쌍따옴표 세 개.
print(multiline)


def func():
    """이 함수는 테스트용입니다."""
    pass


print(
    func.__doc__
)  # doc string 출력. 함수의 첫 번째 줄에 있는 문자열을 doc string라고 함. 첫 줄이 문자열이 아니면 None 이라고 뜸.

# 문자열 연결
print("Hello" + " Python")

# 문자열 반복
print("Hello" * 10)
print("*" * 50)

# 문자열끼리만 + 가능
# print("Hello" + 10)
print("Hello" + str(10))

print("10" + "2")
print(int("10") + int("2"))

# 문자열 포맷팅(f-string)
name = "pororo"
age = 23

print(f"이름 : {name}, 나이 : {age}")
print(f"내년 나이: {age+1}살")
print(f"{name.upper()}")

pi = 3.141592
print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789

print(f"{num:,}")  # 단위 표시 컴마
print(f"{num:15d}") # 15칸 확보 후 오른쪽 정렬
print(f"{num:<15d}") # `` 왼쪽 정렬
print(f"{num:015d}") # 0으로 채운 후 오른쪽 정렬
print(f"{num:15,d}") # 1000 단위 컴마 + 오른쪽 정렬