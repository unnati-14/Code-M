def solve(s):
    d = {}
    for i in s:
        if d[i] in s:
            d[i] += 1
        else:
            d[i] = 1
    for i in s:
        if d[i] > 1:
            return i
    return -1