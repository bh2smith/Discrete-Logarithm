def egcd(a, b): #Euclidean GCD
    if a == 0:
        return (b, 0, 1)
    else:
        d, y, x = egcd(b % a, a)
        return (d, x - (b // a) * y, y)

def inv(a, m):  #Modular inverse for a mod m
    d, x, y = egcd(a, m)
    if d != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def primesTo(n):  #Seive generating primes
	z = [0]*(n+1)
	k = 2
	while k<= n:
		for i in range(k,len(z),k):
			z[i] =  k
		j=k+1
		while j < len(z)-1:
			if z[j]==0:
				k = j
				z[k] = k
				break
			j+=1
		if j == len(z)-1:
			break

	l = []
	for i in range(2,len(z)):
		if z[i]==i:
			l.append(i)
	return l


def primeFactor(n, P): #This actually shaves off some time
	if len(Paux)<5:
		Paux = [2,3,5,7,11,13]
	for i in range(int(len(Paux)/2) +1):
		a,b = Paux[i], Paux[-i-1]
		if n% a ==0 or n % b == 0:
			if n%a == 0:
				return a
			if n%b ==0 :
				return b
	return n

def contract(L,k): #contract list of primes to specified k
	c=1
	while L[-c] > k:
		c+=1
	return L[:-c]


X = primesTo(100001)

for _ in range(input()):

	a,b,g = map(int,raw_input().split(' '))

	sqg = int(g**0.5)			# square root of g
	P = contract(X,sqg)			# primes upto root g
	pfg = primeFactor(g, P)		# a prime factor of g
	ag = pow(a,sqg,g)			# this is a^g mod g

	lasta = 1
	lastb = b
	i = 0
	if pfg == g:            #If g is prime
		
		ainv = pow(a,g-2,g)						#inverse of a mod g
		
		lb = [b]
		for j in range(sqg):					#generate list of powers ba^{-j}
			lb.append((lastb*ainv )% g)
			lastb = (lastb*ainv) % g

		flag = False
		while not flag and i<=sqg:				# check for first a^{\sqrt{g}i} equal to some ba^{-j}
			if lasta in lb:				
				print i*sqg + lb.index(lasta)
				flag = True
				break		
			lasta = (lasta*ag) %g
			i+=1
	
	else:                  	# g is not prime
		ainv = inv(a,g)							# must compute the inverse via euclidean algorithm

		bucket = {k:{} for k in range(pfg)}		# Hash table for values of ba^{-j} mod pfg
		for j in range(sqg):
			lbmod = lastb % pfg
			if lastb not in bucket[lbmod]:		# Records only first occurence of each value (i.e. smallest solution)
				bucket[lbmod][lastb] = j
			lastb = (lastb*ainv) % g

		flag = False
		while not flag and i <= sqg:			# check hash table for first a^{\sqrt{g}i} equal to some ba^{-j}
			lamod = lasta % pfg
			if lasta in bucket[lamod]:
				print i*sqg + bucket[lamod][lasta]
				flag = True
				break		
			lasta = (lasta*ag) % g
			i+=1
	
	if not flag:		# When there was no solution.
			print -1
