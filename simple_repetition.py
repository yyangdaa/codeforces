import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def parse_input():
    t = int(input())
    test_cases = []
    for _ in range(t):
        x, k = map(int, input().split())
        test_cases.append((x, k))
    return test_cases

def run():
    test_cases = parse_input()
    for x, k in test_cases:
        if k != 1:
            print("NO")
        else:
            print("YES" if is_prime(x) else "NO")

if __name__ == "__main__":
    run()