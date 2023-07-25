import math
def main():
    n,k=map(int,input().split())
    # ones = 0
    # for i in range(1, n + 1):
    #     ones += math.ceil(i / k)
    # print(ones)
    a=[0]*n
    # if n%2==0:
    #     ones=0
    #     for i in range(n//2):
    #         if math.ceil((i+1)/k)>ones:
    #             a[i]=1
    #             a[n-i-1]=1
    #             ones+=1
    #     print(a)
    #     return
    # ones=0
    # for i in range(n//2):
    #     if math.ceil((i+1)/k)>ones:
    #         a[i]=1
    #         a[n-i-1]=1
    #         ones+=1
    # # print(a)
    # c=math.ceil((n//2+1)/k)
    # w=0
    # for i in range(n//2+1):
    #     if a[i]==1:w+=1
    # print(w,c)
    # if c>w:
    #     a[n//2]=1
    # print(a)
    # n, k = map(int, input().split())
    v = [0] * n
    ct = 0
    for i in range(n):
        if i % k == 0:
            ct += 1
            v[i] = 1
    if v[n - 1] != 1:
        v[n - 1] = 1
        ct += 1
    # print(v)
    
    c = 0
    for i in range(n - 1, -1, -1):
        if v[i] == 1:
            c += 1
        j = n - i - 1
        
        if math.ceil(float(j) / float(k)) > c:
            c += 1
            ct += 1
    
    print(ct)

for _ in range((int(input()))):
    main()
