#SECPASS
t=int(input())
for testcase in range(t):
    n=int(input())
    word=input()
    substr = []
    freq = []
    for i in range(n//2):
        substr.append(word[:i+1])
        freq.append(word.count(substr[-1]))
    print(substr)
    print(freq)
    maxindex=0
    for i in range(n//2):
        if freq[i]>=freq[maxindex]:
            maxindex=i
    if freq[maxindex]==1:
        print(word)
    else:
        print(substr[maxindex])
