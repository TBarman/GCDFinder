def prime_factorization(n):
    primeFactors = []
    remainder = n
    while remainder != 1:
        for i in range(2, n + 1):
            while remainder%i == 0:
                primeFactors.append(i)
                remainder = remainder/i
    return primeFactors

print(prime_factorization(3072))

def common_factors(n, m):
    nPrime = prime_factorization(n)
    mPrime = prime_factorization(m)
    commonFactors = []
    for factor in nPrime:
        if factor in mPrime:
            commonFactors.append(factor)
            mPrime.remove(factor)
    return commonFactors

def uncommon_factors(n, m):
    nPrime = prime_factorization(n)
    mPrime = prime_factorization(m)
    commonFactors = common_factors(n, m)
    uncommonFactors = []
    for factor in commonFactors:
        nPrime.remove(factor)
        mPrime.remove(factor)
    for factor in nPrime:
        uncommonFactors.append(factor)
    for factor in mPrime:
        uncommonFactors.append(factor)
    return uncommonFactors

print(uncommon_factors(36, 198))


def gcd2(n, m):
    commonFactors = common_factors(n, m)
    gcd = 1
    for factor in commonFactors:
        gcd *= factor
    return gcd

print(gcd2(21, 19))

def lcm2(n, m):
    nPrime = prime_factorization(n)
    mPrime = prime_factorization(m)
    uncommonFactors = uncommon_factors(n, m)
    commonFactors = common_factors(n, m)
    noDupCF = []
    lcm = 1
    for factor in commonFactors:
        if factor not in noDupCF:
            noDupCF.append(factor)
    for factor in commonFactors:
        lcm *= factor
    for factor in uncommonFactors:
        lcm *= factor
    return lcm

print(lcm2(21, 14))


