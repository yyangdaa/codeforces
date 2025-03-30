import sys
import math

def get_primes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for p in range(i * i, n + 1, i):
                is_prime[p] = False
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def func():
    n = int(sys.stdin.readline())
    
    if n == 2:
        print("2 1")
        return
    elif n == 3:
        print("2 1 3")
        return

    primes = get_primes((n + 1) // 2)
    target = primes[-1]  # largest prime ≤ (n+1)//2

    res = []

    for i in range(1, (2 * target) // 2):
        res.append(i)
        res.append(2 * target - i)

    res.append(target)

    for i in range(2 * target, n + 1):
        res.append(i)

    print(" ".join(map(str, res)))

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        func()

if __name__ == "__main__":
    main()
