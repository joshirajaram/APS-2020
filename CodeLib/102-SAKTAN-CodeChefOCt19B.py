# https://www.codechef.com/OCT19B/problems/SAKTAN/

linp = lambda a:list(map(int,input().split(' ')))
minp = lambda a:map(int,input().split(' '))
inp = lambda a:int(input())
MD=10**9+7

t=inp(0)
for _ in range(t):
    n,m,q=minp(0)
    rlst=[0 for i in range(n)]
    clst=[0 for i in range(m)]
    for i in range(q):
        r,c=minp(0)
        rlst[r-1]+=1
        clst[c-1]+=1
    rc,cc=0,0
    for i in rlst:
        if i%2==0:
            rc+=1
    for i in clst:
        if i%2==0:
            cc+=1
    print(rc*(m-cc) + cc*(n-rc))
