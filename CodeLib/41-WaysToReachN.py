N=int(input())
A=list(map(int,input().split()))
Table=[0]*(N+1)
Table[0]=1
l=[]
for i in A:
	for j in range(i,N+1):
		Table[j]+=Table[j-i]
print(Table[N])
print(Table)
