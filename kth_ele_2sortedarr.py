def solve(arr1,arr2,n,m,k):
    p1,p2 = 0,0
    ct = 0
    while p1<n and p2<m:
        if arr1[p1]<arr2[p2]:
            ct += 1
            if ct == k:
                return arr1[p1]
            p1 += 1
        else:
            ct += 1
            if ct ==k:
                return arr2[p2]
            p2 += 1
    while p1<n:
        ct += 1
        if ct == k:
            return arr1[p1]
        p1 += 1
    while p2 < m:
        ct += 1
        if ct == k:
            return arr2[p2]
        p2 += 1