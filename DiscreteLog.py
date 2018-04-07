# TODO - Make this into an actual library (i.e. not reading RawInput)
# pylint: disable=invalid-name

def egcd(a, b):
    # Euclidean GCD
    if a == 0:
        return (b, 0, 1)
    else:
        d, y, x = egcd(b % a, a)
        return (d, x - (b // a) * y, y)

def inv(a, m):
    # Modular inverse for a mod m
    d, x, y = egcd(a, m)
    if d != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def primesTo(n):
    # Sieve generating primes
    z = [0]*(n+1)
    k = 2
    while k <= n:
        for i in range(k, len(z), k):
            z[i] = k
        j = k + 1
        while j < len(z) - 1:
            if z[j] == 0:
                k = j
                z[k] = k
                break
            j += 1
        if j == len(z) - 1:
            break

    l = []
    for i in range(2, len(z)):
        if z[i] == i:
            l.append(i)
    return l


def primeFactor(n, Paux):
    # This actually shaves off some time
    if len(Paux) < 5:
        Paux = [2, 3, 5, 7, 11, 13]
    for i in range(int(len(Paux)/2) + 1):
        a, b = Paux[i], Paux[-i-1]
        if n % a == 0 or n % b == 0:
            if n % a == 0:
                return a
            if n % b == 0:
                return b
    return n

def contract(L, k):
    """Contract list of primes L to have maximum k"""""
    c = 1
    while L[-c] > k:
        c += 1
    return L[:-c]


X = primesTo(100001)

for _ in range(input()):
    a, b, g = map(int, raw_input().split(' '))

    root_g = int(g**0.5)
    primes = contract(X, root_g)
    pfg = primeFactor(g, primes)
    ag = pow(a, root_g, g)

    prev_a, prev_b, i = 1, b, 0
    if pfg == g:
        a_inv = pow(a, g-2, g)

        lb = [b]
        # generate list of powers ba^{-j}
        for j in range(root_g):
            lb.append((prev_b * a_inv) % g)
            prev_b = (prev_b * a_inv) % g

        # check for first a^{\sqrt{g}i} equal to some ba^{-j}
        flag = 0
        while not flag and i <= root_g:
            if prev_a in lb:
                print(i * root_g + lb.index(prev_a))
                flag = 1
                break
            prev_a = (prev_a * ag) % g
            i += 1

    else:
        # g is not prime
        #  must compute the inverse via euclidean algorithm
        a_inv = inv(a, g)

        # Initialize Hash table for values of ba^{-j} mod pfg
        bucket = {k:{} for k in range(pfg)}
        for j in range(root_g):
            lbmod = prev_a % pfg
            # Only record first occurrence of each value (i.e. smallest solution)
            if prev_b not in bucket[lbmod]:
                bucket[lbmod][prev_b] = j
            prev_b = (prev_b * a_inv) % g

        flag = 0
        # check hash table for first a^{\sqrt{g}i} equal to some ba^{-j}
        while not flag and i <= root_g:
            lamod = prev_a % pfg
            if prev_a in bucket[lamod]:
                print(i * root_g + bucket[lamod][prev_a])
                flag = 1
                break
            prev_a = (prev_a * ag) % g
            i += 1

    if not flag:
        # When there was no solution.
        print(-1)
