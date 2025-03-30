def find_k(x, y):
    dp = [[[False]*2 for _ in range(2)] for _ in range(62)]
    back = [[[(0,0,0)]*2 for _ in range(2)] for _ in range(62)]
    dp[0][0][0] = True

    for i in range(61):
        for cx in range(2):
            for cy in range(2):
                if not dp[i][cx][cy]:
                    continue
                bit_x = (x >> i) & 1
                bit_y = (y >> i) & 1
                for kbit in range(2):
                    sum_x = bit_x + kbit + cx
                    sum_y = bit_y + kbit + cy
                    if (sum_x & 1) & (sum_y & 1):
                        continue
                    dp[i+1][sum_x >> 1][sum_y >> 1] = True
                    back[i+1][sum_x >> 1][sum_y >> 1] = (cx, cy, kbit)

    carry_x, carry_y = -1, -1
    for cx in range(2):
        for cy in range(2):
            if cx == 1 and cy == 1:
                continue
            if dp[61][cx][cy]:
                carry_x, carry_y = cx, cy
                break
        if carry_x != -1:
            break

    if carry_x < 0:
        return -1

    k = 0
    for i in range(60, -1, -1):
        px, py, kbit = back[i+1][carry_x][carry_y]
        if kbit:
            k |= (1 << i)
        carry_x, carry_y = px, py

    return k

def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        out.append(str(find_k(x, y)))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
