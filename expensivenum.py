import sys
input = sys.stdin.readline

def parse_input():
    t = int(input())
    test_cases = []
    for _ in range(t):
        k = input().strip()
        test_cases.append(k)
    return test_cases

def run():
    test_cases = parse_input()
    for k in test_cases:
        b = 0
        cnt = 0
        for c in k:
            if c == '0':
                cnt += 1
            else:
                b = max(b, cnt + 1)
        print(len(k) - b)

if __name__ == "__main__":
    run()
