class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if int(s) > finish:
            return 0

        finish_digits = len(str(finish))
        start_digits = len(str(start))
        start_str = str(start)
        finish_str = str(finish)

        max_middle_digits = min(finish_digits - len(s) - 1, finish_digits - start_digits - 1)
        if max_middle_digits == -1:
            print("Start and finish have the same digit length")
            if start < int(s) and int(s) < finish:
                return 1
            else:
                return 0

        count = 0

        if int(finish_str[0]) == limit:
            last_digit_factor = limit - 1
        else:
            last_digit_factor = min(int(finish_str[0]), limit)

        if start < int(s): 
            print("start < s: count += 1")
            count += 1
            start_digit_factor = limit
        else:
            start_digit_factor = limit - int(start_str[0])

        print(f"Initial count: {count}")
        print(f"start_digit_factor: {start_digit_factor}")
        print(f"last_digit_factor: {last_digit_factor}")
        print(f"max_middle_digits: {max_middle_digits}")

        if max_middle_digits == 0:
            print("Handling edge case where max_middle_digits == 0")
            count += last_digit_factor
            if int(finish_str[0]) >= limit and int(finish_str[1:]) > int(s):
                print("Additional count from edge case condition met")
                count += 1
        else:
            count = 1  # Base count for start_same_digit_special case
            if start_digits > len(s):
                print("Calculating special_case_front...")
                count *= self.special_case_front(start_str[1:], limit, s)
            print("Multiplying by standard range combinations...")
            count *= start_digit_factor * last_digit_factor * (limit ** (max_middle_digits - 1))
            if finish_digits > len(s):
                print("Calculating special_case_back...")
                count += self.special_case_back(finish_str[1:], limit, s)

        print("Final computed count:", count)
        return count

    def special_case_front(self, number: str, limit: int, s: str) -> int:
        remaining_digits = len(number) - len(s)
        print(f"special_case_front: number={number}, remaining_digits={remaining_digits}")

        if remaining_digits == 0 and int(number[1:]) <= int(s):
            return 1
        elif remaining_digits == 0 and int(number[1:]) > int(s):
            return 0
        else:
            current_digit = int(number[1])
            if current_digit <= limit:
                result = (limit - current_digit) * (limit ** (remaining_digits - 1)) + self.special_case_front(number[1:], limit, s)
                print(f"Recursing front: current_digit={current_digit}, result={result}")
                return result
            else:
                return 0

    def special_case_back(self, number: str, limit: int, s: str) -> int:
        remaining_digits = len(number) - len(s)
        print(f"special_case_back: number={number}, remaining_digits={remaining_digits}")

        if remaining_digits == 0 and int(number[1:]) >= int(s):
            return 1
        elif remaining_digits == 0 and int(number[1:]) < int(s):
            return 0
        else:
            current_digit = int(number[1])
            if current_digit > limit:
                return limit ** remaining_digits
            else:
                result = (current_digit - 1) * self.special_case_front_back(number[1:], limit, s)
                print(f"Recursing back: current_digit={current_digit}, result={result}")
                return result