@Cache
def double(x):
    return x * 2

# is equivalent to

def double(x):
    return x * 2
double=Cache(double)



@Cache(max_hits=100, timeout=50)
def double(x):
    return x * 2

# is equivalent to

def double(x):
    return x * 2
double = Cache(max_hits=100, timeout=50)(double)
