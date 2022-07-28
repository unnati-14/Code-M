def findTriplets(arr, n):
    s = sorted(arr)
    for i1, e1 in enumerate(s):
        i2 = i1+1
        i3 = n-1
        while i2 < i3:
            summ = s[i1] + s[i2] +s[i3]
            if summ == 0:
                return True
            elif summ >0:
                i3 -= 1
            else:
                i2 += 1
    return False
