t = int(input())

for _ in range(t):
    x, y, a = map(int, input().split())
    D = a

    full_cycles = D // (x + y)
    total_dug = full_cycles * (x + y)

    if total_dug + x > D:
        print("NO") 
    else:
        print("YES") 
