t=int(input())
for _ in range(t):
    p,m,v=map(int,input().split())
    print(v*(m-p+1))