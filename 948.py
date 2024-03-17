class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result, right, left = 0, len(tokens) - 1, 0
        tokens.sort()

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                result += 1

            elif left < right and result > 0:
                result -= 1
                power += tokens[right]
                right -= 1
            else:
                return result

        return result


# 948. Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/description/

# Approach: Two Pointers
# 1. Sort the tokens
# 2. While left <= right
# 3. If power >= tokens[left], increment result, increment left, decrement power
# 4. If left < right and result > 0, decrement result, increment power, decrement right
# 5. Else return result
# 6. Return result
# Time: O(NlogN)
# Space: O(1)
