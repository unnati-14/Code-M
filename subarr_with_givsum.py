def solve(arr,n,s):
    l,r = 0,0
    c = 0
    while r < n:
        c += arr[r]
        while c > s:
            c -= arr[l]
            l += 1
        if s == 0:
            return [-1]
            break
        if c == s:
            return [l+1,r+1]
        r += 1
    return [-1]