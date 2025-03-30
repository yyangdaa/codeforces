def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    index = 1
    answers = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1

        arr = list(map(int, data[index:index+n]))
        index += n
        
        result = max(arr) - min(arr)
        answers.append(str(result))
    
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
