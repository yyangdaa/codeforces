import sys

def next_first(first):
    x, y = first
    if y == 1:
        return (1, x + 3)
    else:
        return (x + 3, y - 3)

def next_next(next_cell):
    x, y = next_cell
    if y == 2:
        if x % 3 == 1:
            return (x + 1, y - 1)
        else:
            return (x, y + 2)
    elif y == 1:
        return (1, x + 3)
    elif y % 3 == 1:
        return (x + 2, y - 2)
    else:
        if x % 3 == 1:
            return (x + 1, y - 3)
        else:
            return (x, y + 2)

def calc_distance(p):
    x, y = p
    dist = x + y
    if x % 3 == 2 and y % 3 == 2:
        dist += 2
    return dist

def func():
    n = int(sys.stdin.readline())
    vec = list(map(int, sys.stdin.readline().split()))
    
    print("1 1")
    
    first = (1, 4)
    next_cell = (1, 2)
    
    for idx in range(1, n):
        i = vec[idx]
        if i == 0:
            print(f"{first[0]} {first[1]}")
            first = next_first(first)
        else:
            if calc_distance(first) < calc_distance(next_cell):
                print(f"{first[0]} {first[1]}")
                first = next_first(first)
            else:
                print(f"{next_cell[0]} {next_cell[1]}")
                next_cell = next_next(next_cell)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        func()

if __name__ == "__main__":
    main()
