##1.
a = int(input())
b = list(map(int, input().split()))
c = b[0]
d = b[0]
for i in b[1:]:
    if c < i :
        c = i
    elif d > i :
        d = i

print(c,d)
print(max(b),min(b))
 
##2.
a = list(map(int,input().split()))
b = 0
for i in range(len(a)):
    if max(a) == a[i]:
        b = i + 1
print(max(a),b)

##3.
a= int(input())
b = int(input())
c = int(input())

v = list(str(a*b*c))
m = [0,0,0,0,0,0,0,0,0,0]

for i in v :
    m[int(i)] = m[int(i)]+1

for i in m:
    print(i)

##4.
a = 42
b = []
c = []

for i in range(10):
    h = int(input())
    b.append(h)
for i in b:
    n = i%42
    c.append(n)

q = set(c)
v= list(q)
print(len(v))

##5.


##6.


##7.
num = int(input())
num2 = 0
list1 = []
list2 = []
for i in range(num):
    num2 = int(input())
    list1.append(num2)

num3 = sum(list1)

num4 = num3/num

for i in range(list1):
    if list1 > num4:
        list2.append(i)

num5 = len(list1)/len(list2)

