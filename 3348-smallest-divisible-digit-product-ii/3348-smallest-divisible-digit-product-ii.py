class Solution(object):
    def smallestNumber(self, num, t):

        # Prime factorization of each digit
        digit_factors = [
            {},                  # 0
            {},                  # 1
            {2: 1},              # 2
            {3: 1},              # 3
            {2: 2},              # 4
            {5: 1},              # 5
            {2: 1, 3: 1},        # 6
            {7: 1},              # 7
            {2: 3},              # 8
            {3: 2}               # 9
        ]

        # --------------------------------------------------
        # 1. Factorize t
        # --------------------------------------------------

        required = {
            2: 0,
            3: 0,
            5: 0,
            7: 0
        }

        x = t

        for p in (2, 3, 5, 7):
            while x % p == 0:
                required[p] += 1
                x //= p

        # If t contains another prime factor,
        # it can never be obtained from digits 1-9.
        if x != 1:
            return "-1"

        # --------------------------------------------------
        # 2. Convert prime factors into minimum digits
        # --------------------------------------------------

        def get_factor_digits(cnt):

            c2 = cnt[2]
            c3 = cnt[3]

            # 2^3 -> 8
            count8 = c2 // 3
            remaining2 = c2 % 3

            # 3^2 -> 9
            count9 = c3 // 2
            remaining3 = c3 % 2

            # 2^2 -> 4
            count4 = remaining2 // 2
            remaining2 = remaining2 % 2

            count2 = remaining2
            count6 = 0

            # 2 * 3 -> 6
            if count2 == 1 and remaining3 == 1:
                count2 = 0
                remaining3 = 0
                count6 = 1

            # 3 * 4 -> 6 * 2
            #
            # Example:
            # 3 * 4 = 12
            # Instead of digits 3,4
            # use digits 2,6
            #
            # This is smaller and uses the same number of digits.
            if remaining3 == 1 and count4 == 1:
                count2 = 1
                count6 = 1
                remaining3 = 0
                count4 = 0

            return {
                2: count2,
                3: remaining3,
                4: count4,
                5: cnt[5],
                6: count6,
                7: cnt[7],
                8: count8,
                9: count9
            }

        # --------------------------------------------------
        # 3. Construct digits in increasing order
        # --------------------------------------------------

        def construct(factors):

            result = []

            for d in range(2, 10):
                result.append(str(d) * factors[d])

            return ''.join(result)

        # Minimum digits required for t
        minimum_factors = get_factor_digits(required)
        minimum_length = sum(minimum_factors.values())

        # If we need more digits than num has,
        # the answer must have one more digit.
        if minimum_length > len(num):
            return construct(minimum_factors)

        # --------------------------------------------------
        # 4. Count prime factors in num
        # --------------------------------------------------

        prefix = {
            2: 0,
            3: 0,
            5: 0,
            7: 0
        }

        for ch in num:
            d = int(ch)

            for p, count in digit_factors[d].items():
                prefix[p] += count

        # --------------------------------------------------
        # 5. If num itself is valid, return it
        # --------------------------------------------------

        first_zero = num.find('0')

        if first_zero == -1:

            valid = True

            for p in (2, 3, 5, 7):
                if prefix[p] < required[p]:
                    valid = False
                    break

            if valid:
                return num

        else:
            # We cannot keep a zero in the answer.
            pass

        # --------------------------------------------------
        # 6. Change one digit from right to left
        # --------------------------------------------------

        for i in range(len(num) - 1, -1, -1):

            current_digit = int(num[i])

            # Remove current digit from prefix
            for p, count in digit_factors[current_digit].items():
                prefix[p] -= count

            space_after = len(num) - 1 - i

            # If this position is after the first zero,
            # the prefix would already contain a zero.
            if i > first_zero and first_zero != -1:
                continue

            # Try a larger digit
            for bigger_digit in range(current_digit + 1, 10):

                remaining = {
                    2: max(
                        0,
                        required[2]
                        - prefix[2]
                        - digit_factors[bigger_digit].get(2, 0)
                    ),

                    3: max(
                        0,
                        required[3]
                        - prefix[3]
                        - digit_factors[bigger_digit].get(3, 0)
                    ),

                    5: max(
                        0,
                        required[5]
                        - prefix[5]
                        - digit_factors[bigger_digit].get(5, 0)
                    ),

                    7: max(
                        0,
                        required[7]
                        - prefix[7]
                        - digit_factors[bigger_digit].get(7, 0)
                    )
                }

                suffix_factors = get_factor_digits(remaining)

                needed = sum(suffix_factors.values())

                # Remaining positions can be filled with 1s
                if needed <= space_after:

                    ones = space_after - needed

                    return (
                        num[:i]
                        + str(bigger_digit)
                        + ('1' * ones)
                        + construct(suffix_factors)
                    )

        # --------------------------------------------------
        # 7. If same length is impossible,
        #    create answer with one extra digit
        # --------------------------------------------------

        extra_factors = get_factor_digits(required)
        needed = sum(extra_factors.values())

        return (
            ('1' * (len(num) + 1 - needed))
            + construct(extra_factors)
        )