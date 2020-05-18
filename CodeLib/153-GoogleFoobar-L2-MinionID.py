def numberToBase(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(int(n % b)))
        n //= b
    # print(digits,sorted(digits))
    return ''.join(digits[::-1])

def solution(n, b):
    k, N = len(n), n
    count, prev = 1, {}
    prev[n]=0
    while True:
        x, y = sorted(list(n),reverse=True), sorted(list(n))
        # print x,y
        x, y = int(''.join(x),b), int(''.join(y),b)
        n = numberToBase(x-y, b)
        # print x,y,n
        zeros = ['0']*(k-len(n))
        n = ''.join(zeros)+n
        try:
            tmp = prev[n]
            return count - prev[n]
        except:
            prev[n] = count
        count += 1
        # print(count,prev)
    return count

n=raw_input()
b=int(raw_input())
print(solution(n,b))
