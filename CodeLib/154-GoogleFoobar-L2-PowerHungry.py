def solution(arr):
    pos, neg = [], []
    prod = 1
    for i in arr:
        if i>0:
            pos.append(i)
            prod *= i
        elif i<0:
            neg.append(i)
    for i in neg:
        prod *= abs(i)
    if len(neg)%2==1:
        prod //= abs(max(neg))
    if len(neg)==1 and len(pos)==0:
        prod = max(arr)
    return str(prod)
