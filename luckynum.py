n=int(input())
n=str(n)
c=0
for i in n:
    if i=='4' or i=='7':
        c+=1
if c==4 or c==7 :
    print("YES")
else:
    print("NO")
# print(c) 