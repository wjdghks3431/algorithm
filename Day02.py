# 1. 두수 비교하기
a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print('<')
elif a == b:
    print('==')

# 2. 시험 성적
a = int(input())

if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("F")


# 3. 윤년
a = int(input())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(1)
else:
    print(0)

# 4. 사분면 고르기
a = int(input())
b = int(input())

if a > 0 and b > 0:
    print(1)
elif a < 0 and b > 0:
    print(2)
elif a < 0 and b < 0:
    print(3)
elif a > 0 and b < 0:
    print(4)

# 5. 알람시계
a, b = map(int, input().split())

if b < 45:
    if a == 0:
        print(a+23, b+(60-45))
    else:
        print(a-1, b+(60-45))
else:
    print(a, b-45)

# 6. 오븐 시계
a, b = map(int, input().split())
c = int(input())
d = 0
if b+c >= 60:
    d = a+((b+c)//60)
    if d >= 24:
        print(d-24, (b+c) % 60)
    else:
        print(d, (b+c) % 60)
else:
    print(a, b+c)


# 7. 주사위 세개
a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    print(10000+(a*1000))
elif a == b and b != c and c != a:
    print(1000+(a*100))
elif a != b and b != c and c == a:
    print(1000+(a*100))
elif a != b and b == c and c != a:
    print(1000+(b*100))
else:
    if a > b and a > c:
        print(100*a)
    elif b > a and b > c:
        print(100*b)
    elif c > b and c > a:
        print(100*c)
