# Codeforces Python Contest Template
# Save this file as `template.py` and copy-paste the parts you need.
# Stay calm — you got this.

import sys
input = sys.stdin.readline

# ==============================================
# 📥 PARSE INPUT: Single array per test case
# Example:
# 2          <- number of test cases
# 5          <- size of first array
# 1 2 3 4 5  <- first array
# 3
# 9 8 7
# ==============================================

def parse_input():
    t = int(input())
    test_cases = []
    for _ in range(t):
        n = int(input())                      # n = size of array
        arr = list(map(int, input().split())) # arr = list of integers
        test_cases.append((n, arr))
    return test_cases


# ==============================================
# 🧠 LOGIC FUNCTION: Write your solution here
# This is where you implement your per-test-case logic.
# You can use one of the output styles below.
# ==============================================

def run():
    test_cases = parse_input()
    for n, arr in test_cases:
        # 🚧 WRITE YOUR LOGIC BELOW 🚧

        # Example 1: Output a single number
        # print(sum(arr))

        # Example 2: Output YES or NO
        # if all(x == arr[0] for x in arr):
        #     print("YES")
        # else:
        #     print("NO")

        # Example 3: Output transformed array
        # doubled = [x * 2 for x in arr]
        # print(' '.join(map(str, doubled)))

        # Example 4: Output multiple lines per test case
        # for num in arr:
        #     print(num)
        # print("---")  # Optional separator

        pass  # Remove this when you start writing

# ==============================================
# 🔁 MAIN ENTRY POINT
# ==============================================

if __name__ == "__main__":
    run()
