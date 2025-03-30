import sys

def solve():
    input_data = sys.stdin.read().strip().splitlines()
    t = int(input_data[0])
    
    if not (1 <= t <= 10000):
        sys.stdout.write("NO\n")
        return
    
    idx = 1
    total_cells = 0
    results = []
    
    for _ in range(t):
        n, m = map(int, input_data[idx].split())
        idx += 1
        
        if not (1 <= n <= 50 and 1 <= m <= 50):
            results.append("No")
            idx += n
            continue
        
        grid = input_data[idx : idx + n]
        idx += n
        
        valid_grid = True
        for row in grid:
            if len(row) != m or any(ch not in '01' for ch in row):
                valid_grid = False
                break
        
        if not valid_grid:
            results.append("No")
            continue
        
        total_cells += n * m
        if total_cells > 10000:
            results.append("No")
            continue
        
        possible = True
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    row_ok = True
                    for c in range(j + 1):
                        if grid[i][c] == '0':
                            row_ok = False
                            break
                    
                    col_ok = True
                    for r in range(i + 1):
                        if grid[r][j] == '0':
                            col_ok = False
                            break
                    
                    if not row_ok and not col_ok:
                        possible = False
                        break
            if not possible:
                break
        
        results.append("Yes" if possible else "No")
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
