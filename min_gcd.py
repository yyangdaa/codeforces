import sys
import math
input = sys.stdin.readline

def parse():
    t = int(input())
    cases = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        cases.append((n, arr))
    return cases

def solve(n, arr):
    g = arr[0]
    for x in arr[1:]:
        g = math.gcd(g, x)
    b = [x // g for x in arr]
    m = min(b)
    bad = [x for x in b if x % m != 0]
    if not bad:
        return "Yes"
    cnt_m = b.count(m)
    if cnt_m >= 2:
        return "Yes"
    if len(bad) >= n - 1:
        return "No"
    multiples = [x for x in b if x % m == 0 and x != m]
    if not multiples:
        return "No"
    gg = 0
    for x in multiples:
        gg = math.gcd(gg, x // m)
        if gg == 1:
            return "Yes"
    return "No"

def main():
    cases = parse()
    for n, arr in cases:
        print(solve(n, arr))

if __name__ == "__main__":
    main()
