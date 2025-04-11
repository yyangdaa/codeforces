import sys
from collections import Counter

input = sys.stdin.readline

def parse_input():
    t = int(input())
    cases = []
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        cases.append((n, k, arr))
    return cases
#
def canDo(x, arr, k):
    if x == 0:
        return True
    parts = 0
    seen = [0] * x
    left = x
    for num in arr:
        if num < x and not seen[num]:
            seen[num] = 1
            left -= 1
        if left == 0:
            parts += 1
            if parts >= k:
                return True
            seen = [0] * x
            left = x
    return False

def maxMex(arr, k):
    freq = Counter(arr)

    ptr = 0
 #   
    # while ptr in freq and freq[ptr] >= k:
    #     ptr += 1
##
    ###
    while freq[ptr] >= k:
        ptr += 1

    lo = 0
    hi = ptr + 1

    while lo < hi:
        um = (lo + hi) // 2
        if canDo(um, arr, k):
            lo = um + 1
        else:
            hi = um
    return lo - 1

def run():
    tests = parse_input()
    for _, k, arr in tests:
        print(maxMex(arr, k))

if __name__ == "__main__":
    run()
