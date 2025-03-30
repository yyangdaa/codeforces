def find_mex(a):
    s = set(a)
    x = 0
    while x in s:
        x += 1
    return x

def solve_case(a):
    ops = []
    while len(a) > 1:
        m = find_mex(a)
        ops.append((1, len(a)))
        a = [m]
    return ops

def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    ans = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        if n == 1:
            ans.append("0")
        else:
            ops = solve_case(arr)
            ans.append(str(len(ops)))
            for x, y in ops:
                ans.append(f"{x} {y}")
    print("\n".join(ans))

if __name__ == "__main__":
    solve()
