# 아스키 코드

a = input()
print(ord(a))

# 숫자의 합

n = input()

print(sum(map(int, input())))

# 2)
n = input()
nums = input()
total = 0
for i in nums:
    total += int(i)  # total= total+int(i)
print(total)


# 알파벳 찾기

word = input()
alphabet = list(range(97, 123))  # 아스키코드 숫자 범위

for x in alphabet:
    print(word.find(chr(x)))

# 문자열 반복

t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
