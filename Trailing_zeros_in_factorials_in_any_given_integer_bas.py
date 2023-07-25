def trailing_zeros(n, b):
    # Factorize the base
    base_factors = factorize(b)

    # For each prime factor, find the highest power that divides n!
    zeros = float('inf')
    for prime, power in base_factors.items():
        prime_power_in_n = 0
        i = prime
        while i <= n:
            prime_power_in_n += n // i
            i *= prime
        zeros = min(zeros, prime_power_in_n // power)

    return zeros

def factorize(b):
    factors = {}
    i = 2
    while i * i <= b:
        if b % i:
            i += 1
        else:
            b //= i
            factors[i] = factors.get(i, 0) + 1
    if b > 1:
        factors[b] = factors.get(b, 0) + 1
    return factors
