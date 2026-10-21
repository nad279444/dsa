"""Generate every prime below n using the Sieve of Eratosthenes.

Approach: start with a boolean table where only indices >= 2 are marked prime
(0 and 1 are not prime). Scanning i from 2 upward, any i still marked prime is
appended to the result, then all multiples of i starting at i * i are marked
non-prime — multiples below i * i already have a smaller prime factor and were
struck out by an earlier pass, so starting at i * i skips that work.
Time: O(n log log n); Space: O(n) for the boolean table.
"""


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
    # All primes strictly below 13
    assert generate_prime(13) == [2, 3, 5, 7, 11]

    # All primes strictly below 20
    assert generate_prime(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # Nothing to check below 2
    assert generate_prime(2) == []
    assert generate_prime(3) == [2]

    print("All tests passed")
