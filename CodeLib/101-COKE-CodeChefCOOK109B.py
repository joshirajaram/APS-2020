# https://www.codechef.com/COOK109B/problems/COKE

t=int(input())
for _ in range(t):
    n,m,k,l,r=map(int,input().split(' '))
    #cp=[]
    cheap=10**6
    flag=0
    for I in range(n):
        ci,pi=map(int,input().split(' '))
        #cp.append([pi,ci])
        for j in range(m):
            if ci>(k+1):
                ci-=1
            elif ci<(k-1):
                ci+=1
            else:
                ci=k
        if ci>=l and ci<=r:
            flag=1
            if pi<cheap:
                cheap=pi
        #print(ci,pi,cheap)
    if flag==0:
        print('-1')
    else:
        print(cheap)
