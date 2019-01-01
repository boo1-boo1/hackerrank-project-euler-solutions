t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    n3, n5, n15 = n//3, n//5, n//15
    total = (3*(n3*(n3+1))//2) + (5*(n5*(n5+1))//2) - (15*(n15*(n15+1))//2)
    print(total)
