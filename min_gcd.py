import sys
import math
input = sys.stdin.readline

<<<<<<< HEAD
def parse():
=======
def get_cases():
>>>>>>> 47bfae991d7f2aa624dd55c2dd9cbe7015f956a7
    t = int(input())
    cases = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        cases.append((n, arr))
    return cases

def solve(n, arr):
<<<<<<< HEAD
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
=======
    if n == 2 and sorted(arr) == [1, 2]:
        return "No"
    m = min(arr)
    bad = [x for x in arr if x % m != 0]

    if bad:
        cnt_m = arr.count(m)
        good_count = n - len(bad)
        if (good_count - 1) <= 0:
            return "No"
        if cnt_m >= 2:
            return "Yes"
        second_part = [x // m for x in arr if x % m == 0 and x != m]
        if not second_part:
            return "No"
        g = 0
        for val in second_part:
            g = math.gcd(g, val)
            if g == 1:
                return "Yes"
        return "Yes" if g == 1 else "No"
    else:
        g = arr[0]
        for val in arr[1:]:
            g = math.gcd(g, val)
            if g == m:
                break
        return "Yes" if g == m else "No"

def main():
    cases = get_cases()
>>>>>>> 47bfae991d7f2aa624dd55c2dd9cbe7015f956a7
    for n, arr in cases:
        print(solve(n, arr))

if __name__ == "__main__":
    main()
