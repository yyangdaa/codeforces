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

        arr = list(map(int, data[index:index+n]))
        index += n
        if n == 1:
            results.append(str(arr[0]))
            continue
        
        first_parity = arr[0] % 2
        all_same = True
        odd_count = 0
        for x in arr:
            if x % 2 != first_parity:
                all_same = False
            if x % 2 == 1:
                odd_count += 1
        
        if all_same:
            results.append(str(max(arr)))
        else:
            S = sum(arr)
            results.append(str(S - odd_count + 1))
    
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
