class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        longest = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            longest = max(longest, right - left + 1)

        return longest
