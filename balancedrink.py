def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = list(data[idx])
        idx += 1
        
        cnt = {'L': 0, 'I': 0, 'T': 0}
        for c in s:
            cnt[c] += 1
        if len(s) % 3 == 0 and cnt['L'] == cnt['I'] == cnt['T']:
            out.append('0')
            continue
        
        if all(c == s[0] for c in s):
            out.append('-1')
            continue

        current_max = max(cnt.values())
        k = current_max
        required_length = 3 * k
        m = required_length - n
        
        if m < 0 or m > 2 * n:
            out.append('-1')
            continue
        
        needed = {
            'L': k - cnt['L'],
            'I': k - cnt['I'],
            'T': k - cnt['T']
        }
        
        if sum(needed.values()) != m:
            out.append('-1')
            continue

        possible = True
        ops = []
        current_s = s.copy()
        
        for _ in range(m):
            inserted = False

            for i in range(len(current_s) - 1):
                a = current_s[i]
                b = current_s[i + 1]
                if a == b:
                    continue

                if a != 'L' and b != 'L':
                    forced_char = 'L'
                elif a != 'I' and b != 'I':
                    forced_char = 'I'
                else:
                    forced_char = 'T'

                if needed[forced_char] > 0:
                    current_s.insert(i + 1, forced_char)
                    ops.append(i + 1) 
                    needed[forced_char] -= 1
                    inserted = True
                    break
            if not inserted:
                possible = False
                break
        
        if possible and all(v == 0 for v in needed.values()):
            final_cnt = {'L': 0, 'I': 0, 'T': 0}
            for c in current_s:
                final_cnt[c] += 1
            if final_cnt['L'] == final_cnt['I'] == final_cnt['T'] and len(current_s) % 3 == 0:
                out.append(str(len(ops)))
                if ops:
                    out.extend(map(str, ops))
            else:
                out.append('-1')
        else:
            out.append('-1')
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()