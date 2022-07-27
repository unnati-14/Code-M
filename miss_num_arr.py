def solve(arr,n):
    c = 0
    arrsum = sum(arr)
    for i in range(1,n+1):
        c += i
    return c - arrsum