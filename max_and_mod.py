import sys
input = sys.stdin.readline

def get_cases():
    t = int(input())
    cases = []
    for _ in range(t):
        cases.append(int(input()))
    return cases

def check(arr):
    for i in range(2, len(arr)+1):
        if max(arr[i-2], arr[i-1]) % i != i-1:
            return False
    return True

def solve(n):
    if n in [2, 4]:
        return -1
    perm = [1, n] + [i for i in range(2, n)]
    if check(perm):
        return perm
    from itertools import permutations
    for p in permutations(range(1, n+1)):
        if check(p):
            return p
    return -1

def main():
    cases = get_cases()
    for n in cases:
        ans = solve(n)
        if ans == -1:
            print(-1)
        else:
            print(*ans)

if __name__ == "__main__":
    main()
