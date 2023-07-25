for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    # print(a)
    l=a[0]*a[1]
    r=a[len(a)-1]*a[len(a)-2]
    print(max(l,r))
    