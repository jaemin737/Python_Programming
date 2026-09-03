# 반복문 : while문, for문

# while문
# 1 ~ 10 까지의 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    # if i == 6:
    #     break         # 조건문이 완료되어서 정상 종료 된 경우에만 else 실행. break에선 안함.
else:
    print("End")

nums = [1, 3, 4, 5, 7, 9]
target = 2
i = 0
# found = False
while i < len(nums):
    if nums[i] == target:
        print(f"{target} Found")
        found = True
        break
    i += 1
else:
    print(f"{target} Not found")

# if not found:
#     print(f"{target} Not found")

# 1 ~ 10까지의 합

# 짝수만

i = 1
tot = 0
while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1
else:
    print(f"sum : {tot}")

# i = 1
# tot = 0
# while i <= 10:
#     i+=1
#     if i % 2 == 1:
#         continue
#     tot += i
# else:
#     print(f"sum : {tot}")

