def generate_prime(n: int):
    primes = []
    # 0 and 1 are not primes so we start with false
    isPrime = [False, False] + ([True] * (n - 1))

    for i in range(2, n):
        if isPrime[i]:
            primes.append(i)

            # sieve
            for multiple in range(i * i, n + 1, i):
                # rule out all multiples of the prime
                isPrime[multiple] = False

    return primes


if __name__ == "__main__":
    print(generate_prime(13))
