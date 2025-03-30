def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = data[index]
        index += 1
        b = data[index]
        index += 1

        ones_comp1 = 0
        for i in range(n):
            if i % 2 == 0: 
                if a[i] == '1':
                    ones_comp1 += 1
        for i in range(n):
            if i % 2 == 1:
                if b[i] == '1':
                    ones_comp1 += 1

        ones_comp2 = 0
        for i in range(n):
            if i % 2 == 1: 
                if a[i] == '1':
                    ones_comp2 += 1

        for i in range(n):
            if i % 2 == 0:
                if b[i] == '1':
                    ones_comp2 += 1

        avail_comp1 = n // 2         
        avail_comp2 = (n + 1) // 2     

        if ones_comp1 <= avail_comp1 and ones_comp2 <= avail_comp2:
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
