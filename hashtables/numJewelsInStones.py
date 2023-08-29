# LeetCode 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels_set = set()
        jewels_count = int()

        for char in jewels:
            jewels_set.add(char)

        for char in stones:
            if char in jewels_set:
                jewels_count += 1

        return jewels_count
