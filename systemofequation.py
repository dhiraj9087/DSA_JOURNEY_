import math
n, m= map(int, input().split())
answer =0
for a in range(int(math.sqrt(n))+1):
    b = n - a * a
    if a + b * b == m and b >= 0:
        answer += 1
print(answer)
