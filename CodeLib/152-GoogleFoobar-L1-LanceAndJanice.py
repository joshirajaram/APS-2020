def solution(s):
    c = ord('a')
    i, j=0, 26
    lookUp = {}
    for _i in range(1,27):
        lookUp[chr(c+i)] = chr(c+j-_i)
        i+=1
    output = ''
    for i in s:
        if i in lookUp:
            output += lookUp[i]
        else:
            output += i
    return output
