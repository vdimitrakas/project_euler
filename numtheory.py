
def gcd(m,n):
    """Finds the CDG using x's efficient Euclidean Algorithm"""
    rem = 1
    r1 = m
    r2 = n
    while True:
        M = max(r1, r2)
        m = min(r1, r2)
        r = (M-m) % m
        r1 = m
        r2 = r1
        if r == 0:
            break
    return r1