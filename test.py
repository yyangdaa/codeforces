def parse_input():
    import sys
    return sys.stdin.read().split()

def main():
    tokens = parse_input()
    t_index = 0
    test_cases = int(tokens[t_index])
    t_index += 1
    output_lines = []
    
    for _ in range(test_cases):
        n = int(tokens[t_index])
        t_index += 1
        a = list(map(int, tokens[t_index:t_index+n]))
        t_index += n
        b = list(map(int, tokens[t_index:t_index+n]))
        t_index += n

        # --- Step 1. Group indices by the unordered pair key ---
        groups = {}  # key -> list of indices
        for i in range(n):
            key = (min(a[i], b[i]), max(a[i], b[i]))
            groups.setdefault(key, []).append(i)
        
        pairs = []   # to store paired indices as (left, right)
        center = None  # for odd n, index with a[i]==b[i]
        possible = True

        for key, idx_list in groups.items():
            # For indices where the two values are equal, the order doesn’t matter.
            if key[0] == key[1]:
                idx_list.sort()
                # Pair up indices arbitrarily
                while len(idx_list) >= 2:
                    left = idx_list.pop(0)
                    right = idx_list.pop(0)
                    pairs.append((left, right))
                if idx_list:
                    cand = idx_list[0]
                    # For a candidate to be center, we require a[cand]==b[cand]
                    if a[cand] != b[cand]:
                        possible = False
                        break
                    else:
                        # There can be only one center.
                        if center is None:
                            center = cand
                        else:
                            possible = False
                            break
            else:
                # For distinct pairs the total count must be even.
                if len(idx_list) % 2 != 0:
                    possible = False
                    break
                idx_list.sort()
                # Pair them in order; decide orientation so that mirror condition can be met.
                while idx_list:
                    i1 = idx_list.pop(0)
                    i2 = idx_list.pop(0)
                    # One valid ordering is if a[i1]==b[i2]; otherwise, if a[i2]==b[i1], swap.
                    if a[i1] == b[i2]:
                        pairs.append((i1, i2))
                    elif a[i2] == b[i1]:
                        pairs.append((i2, i1))
                    else:
                        possible = False
                        break
                if not possible:
                    break

        # For an odd n, if no center candidate exists then try to find one (must satisfy a[i]==b[i])
        if n % 2 == 1 and center is None:
            for i in range(n):
                if a[i] == b[i]:
                    center = i
                    break
            if center is None:
                possible = False

        if not possible:
            output_lines.append("-1")
            continue

        # --- Step 2. Build the target permutation ---
        # We need to assign the pairs to mirror positions.
        L = n // 2  # number of mirror pairs
        if len(pairs) != L:
            possible = False
            output_lines.append("-1")
            continue

        # (If multiple valid answers exist, we choose one by sorting the pairs.
        # Here we sort descending by the a-value of the left partner—this ordering
        # will (for example) yield the sample output on one test case.)
        pairs.sort(key=lambda pr: a[pr[0]], reverse=True)
        target_perm = [None] * n
        for idx, (left_idx, right_idx) in enumerate(pairs):
            target_perm[idx] = left_idx
            target_perm[n - 1 - idx] = right_idx
        if n % 2 == 1:
            target_perm[L] = center

        # --- Step 3. Transform the current (identity) order into target_perm ---
        # Our allowed operation swaps two indices (affecting both arrays), so we can
        # “sort” the identity permutation into target_perm.
        current_perm = list(range(n))
        swaps = []
        # Build a mapping: value -> current index
        pos = {current_perm[i]: i for i in range(n)}
        for i in range(n):
            if current_perm[i] != target_perm[i]:
                desired = target_perm[i]
                j = pos[desired]
                # Swap current_perm[i] and current_perm[j]
                current_perm[i], current_perm[j] = current_perm[j], current_perm[i]
                swaps.append(f"{i+1} {j+1}")  # using 1-based indexing for output
                pos[current_perm[i]] = i
                pos[current_perm[j]] = j

        if len(swaps) > n:
            output_lines.append("-1")
        else:
            output_lines.append(str(len(swaps)))
            output_lines.extend(swaps)
    
    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
