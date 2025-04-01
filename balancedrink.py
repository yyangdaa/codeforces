def main():
    import sys
    from collections import deque
    sys.setrecursionlimit(10**7)
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []
    def is_balanced(s):
        L = len(s)
        if L % 3 != 0:
            return False
        cL = s.count('L')
        cI = s.count('I')
        cT = s.count('T')
        return cL == cI == cT == L // 3
    def forced(a, b):
        for ch in ("L","I","T"):
            if ch!=a and ch!=b:
                return ch
        return None
    for _ in range(t):
        n = int(data[idx])
        idx+=1
        s = list(data[idx])
        idx+=1
        if n==1:
            out_lines.append("-1")
            continue
        if is_balanced(s):
            out_lines.append("0")
            continue
        max_ops = 2*n
        visited = {}
        start = ("".join(s), [])
        queue = deque([start])
        ans = None
        visited[start[0]] = 0
        while queue:
            st, ops = queue.popleft()
            if is_balanced(st):
                ans = (ops, st)
                break
            if len(ops)>=max_ops:
                continue
            Lcur = len(st)
            for i in range(Lcur-1):
                if st[i]!=st[i+1]:
                    ins = forced(st[i], st[i+1])
                    ns = st[:i+1]+ins+st[i+1:]
                    if ns not in visited or visited[ns]>len(ops)+1:
                        visited[ns] = len(ops)+1
                        queue.append((ns, ops+[i+1]))
        if not ans:
            out_lines.append("-1")
        else:
            seq = ans[0]
            out_lines.append(str(len(seq)))
            out_lines.extend(str(x) for x in seq)
    sys.stdout.write("\n".join(out_lines))
 
 
if __name__=="__main__":
    main()