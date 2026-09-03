# for 문

# for (int i = 0; i < 10; i++)

# for i in iterable 객체:
#   ...
# iterable 객체 : 반복 가능한 거. 문자열, 숫자 ...

for i in range(5):  # 0 ~ 4
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)
# syntax : range(start, stop, step)

# 1 ~ 5
for i in range(1, 6):
    print(i, end=" ")
print()

# 1 ~ 10, 2칸씩
for i in range(1, 11, 2):
    print(i, end=" ")
print()

#  5, 4, 3, 2, 1 거꾸로
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10 까지의 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(f"sum : {tot}")

print(sum(range(1, 11)))

s = "hi12!@한글韓字📖📘"

for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
# 2 * 1 = 2    2 * 2 = 4    2 * 3 = 6 ... 2 * 9 = 18
# 3 * 1 = 2    3 * 2 = 6    3 * 3 = 9 ... 3 * 9 = 27
# ...

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:2d}", end="\t")
    print()
else: 
    print("end")