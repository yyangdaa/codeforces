import sys
input = sys.stdin.readline

def parse_input():
    t = int(input())
    return t

def f(n, x, y):
    if n == 1:
        if x == 1 and y == 1:
            return 1
        if x == 2 and y == 2:
            return 2
        if x == 2 and y == 1:
            return 3
        return 4
    h = 1 << (n - 1)
    b = 1 << (2 * (n - 1))
    if x <= h and y <= h:
        return f(n - 1, x, y)
    if x > h and y > h:
        return b + f(n - 1, x - h, y - h)
    if x > h and y <= h:
        return 2 * b + f(n - 1, x - h, y)
    return 3 * b + f(n - 1, x, y - h)

def g(n, d):
    if n == 1:
        if d == 1:
            return (1, 1)
        if d == 2:
            return (2, 2)
        if d == 3:
            return (2, 1)
        return (1, 2)
    h = 1 << (n - 1)
    b = 1 << (2 * (n - 1))
    if d <= b:
        x, y = g(n - 1, d)
        return (x, y)
    if d <= 2 * b:
        x, y = g(n - 1, d - b)
        return (x + h, y + h)
    if d <= 3 * b:
        x, y = g(n - 1, d - 2 * b)
        return (x + h, y)
    x, y = g(n - 1, d - 3 * b)
    return (x, y + h)

def run():
    t = parse_input()
    for _ in range(t):
        n, q = map(int, input().split())
        for _ in range(q):
            op = input().strip()
            if op == '->':
                x, y = map(int, input().split())
                print(f(n, x, y))
            else:
                d = int(input())
                x, y = g(n, d)
                print(x, y)

if __name__ == "__main__":
    run()
