# 3.분수찾기
X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line-X+1
else:
    a = line-X+1
    b = X

print(a, '/', b, sep='')

# 4.달팽이는 올라가고 싶다
a, b, v = map(int, input().split())
k = 0  # 올라가는 데 걸리는 일수
d = 0  # 올라간 높이
while 1:
    k += 1
    if a*k-b*(k-1) >= v:
        break
print(k)
