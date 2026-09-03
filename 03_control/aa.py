# a = int(input())
# print(f"{a:15,d}")
# print(f"{a:<15,d}")
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# a = int(float(input()))
# print(a)

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# a = input()
# b = int(input())
# print(a*b)

# s = input()
# print(f"길이: {len(s)}")
# print(f"대문자 변환: {s.upper()}")

# s = input()
# print("[" + s.lstrip() + "]")
# print("[" + s.rstrip() + "]")
# print("[" + s.strip() + "]")


a = input()
print(a.isalnum() and (not(a.isalpha())) and (not (a.isdigit())) and len(a) >= 8)
