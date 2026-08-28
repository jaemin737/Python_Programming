# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 소수점까지 나눠줌
print(a % b)  # 나머지
print(a // b)  # 몫만
print(a**b)  # 제곱

# 복합 대입 연산자
a = 0
a += 4
print(a)

a -= 2
print(a)

# 증감 연산자 => 없음
# a++
# b = a++ ?
a += 1

# 비교 연산자
print(3 == 3.0)  # True
print(3 != 4)
print("apple" < "apble")  # False. 사전에서 뒤에 나올수록 큼.
print(1 < 2 < 3)  # True. => 1 < 2 && 2 < 3 => 1 < 2 and 2 < 3
print(1 < 3 < 2)
# print(1 < 3 or 3 < 2)

# 논리 연산자 (and, or, not)
a = True
b = False

print(a and b) # &&
print(a or b) # ||
print(not b) # !

# Short-circuit 테스트
a = 10
b = 0

# print(a / b)

if a > 0 or a / b:  
    print("yes")
else:
    print("no")
# Short-circuit 가능