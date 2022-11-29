# 1. 손익분기점
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)

# 2.벌집
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup:
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)
