def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    pos = 1
    test_cases = []
    max_n = 0
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        s = data[pos]
        pos += 1
        test_cases.append((n, s))
        if n > max_n:
            max_n = n

    div_count = [0] * (max_n + 2) 
    for i in range(1, max_n + 2):  
        for j in range(i, max_n + 2, i):
            div_count[j] += 1

    out_lines = []
    for n, s in test_cases:
        res = []
        b = 0
        res.append("1")
        for i in range(2, n + 1):
            if s[i - 2] != s[i - 1]:
                b += 1
            if b == 0:
                res.append(str(i))
            else:
                res.append(str(div_count[b + 1] + (i - (b + 1))))
        out_lines.append(" ".join(res))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
