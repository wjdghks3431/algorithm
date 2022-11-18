## 1. 구구단
a=int(input())
for i in range(1,10):
    print("%d * %d = %d"%(a,i,a*i))

## 2. A+B
a=int(input())
d = []
r=0
for i in range(a):
    b=int(input())
    c=int(input())
    r = b+c
    d.append(r)
for i in d:
    print(i)

## 3.합
a= int(input())
b=0
for i in range(1,a+1):
    b=b+i
print(b)

## 5. N찍기
a= int(input())

for i in range(1,a+1):
    print(i)

## 6. 기찍N
a= int(input())

for i in range(a,0,-1): ## range(시작(start), 멈춤(stop), 단계(step)(안 적을 시 자동적 +1, -1을 적을시 내림차순)
    print(i)

## 7. A+B
a=int(input())
d = []
r=0
for i in range(a):
    b=int(input())
    c=int(input())
    r = b+c
    d.append(r)

for i in range(0,len(d)):
    print("Case #%d : %d"%(i+1,d[i]))

## 8. A+B
a=int(input())
d = []
e = []
w = []
r = 0
for i in range(a):
    b=int(input())
    c=int(input())
    e.append(b)
    w.append(c)
    r = b+c
    d.append(r)

for i in range(0,len(d)):
    print("Case #%d: %d + %d = %d"%(i+1,e[i],w[i],d[i]))

## 9. *찍기
a=int(input())

for i in range(1,a+1):
    print("*" * i)

## 10. ***


## 11. 
a=int(input())
b=int(input())
c = []
for i in range(a):
    d=int(input())
    c.append(d)
for i in range(len(c)):
    if c[i]<b:
        print(c[i])
    else:
        continue
