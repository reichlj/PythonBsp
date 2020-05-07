from math import sqrt
 
no_primes = [ j for i in range(2,8) for j in range(i*2,101,i)]
primes = [k for k in range(2,101) if k not in no_primes]
print(primes)

n = 100
sqrt_n = int(sqrt(n))
no_primes = [ j for i in range(2,sqrt_n) for j in range(i*2,n+1,i)]
print(no_primes)
primes = [k for k in range(2,n+1) if k not in no_primes]
print(primes)
