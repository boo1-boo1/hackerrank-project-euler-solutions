def evenFibSum(limit):
    if limit < 2:
        return 0
    ef1, ef2 = 0, 2
    total = ef1 + ef2
    
    while ef2 <= limit:
        ef3 = 4 * ef2 + ef1
        if ef3 > limit:
            break
        ef1, ef2 = ef2, ef3
        total += ef2
    
    return total

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(evenFibSum(n))
