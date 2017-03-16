



def is_relative_prime(n, l):
    """
    Returns True if n is a relative prime w.r.t. all elements of list l
    If l is the list of prime that run at least to sqrt(n), then the function is a
    This is slower that the optimal implementation I could come up with
    """
    if l ==[]:
        ans = True
    else:
        return min([max(n,e)%min(n,e) for e in l]) > 0
