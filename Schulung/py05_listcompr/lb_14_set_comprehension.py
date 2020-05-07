s = {x for x in 'set comprehension'}
print(s)

no_primes = { j for i in range(2,8) for j in range(i*2,101,i)}
print(no_primes)
primes = [k for k in range(2,101) if k not in no_primes]
print(primes)

