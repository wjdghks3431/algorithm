# Hello World
print("Hello World!")

# A+B
a, b = map(int, input().split())
print(a+b)

# A-B
a, b = map(int, input().split())
print(a-b)

# A*B
a, b = map(int, input().split())
print(a*b)

# A/B
a, b = map(int, input().split())
print(a/b)

# 사칙연산
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)  # 몫만 구할때는 //를 사용한다
print(a % b)  # 나머지 값만 구할 때는 %를 사용한다

# ??!
a = str(input())
print(a+'??!')

# 1998년생인 내가 태국에서는 2541년생?!
a = int(input())
print(a - 543)

## 킹, 퀸, 록, 비숍, 나이트, 폰
a, b, c, d, e, f = map(int, input().split())

print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)

# 나머지
A, B, C = map(int, input().split())

print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A*B) % C)
print(((A % C) * (B % C)) % C)

# 곱셈
a = input()
b = input()

print(int(a) * int(b[-1]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(int(a) * int(b))

# 고양이
print("\    /\ ")
print(" )  ( ')")
print("(  /  )")
print(" \(__)| ")

# 개
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')  # \'앞에 \을 붙여준다.
print('|"^"`    |')
print("||_/=\\\__|")  # \\ 앞에 \을 하나 더 붙여준다.

# 색싹
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")

# \를 그대로 출력하기 위해선 \\와 같이 두 번 작성해야 한다.

# 또한 " " , 혹은 ' ' 안에 똑같은 것을 출력하기 위해서는 \" 혹은 \' 꼴로 출력해야 한다.

# 마지막으로 띄어쓰기에 유의하여 잘 출력하도록 하자.
