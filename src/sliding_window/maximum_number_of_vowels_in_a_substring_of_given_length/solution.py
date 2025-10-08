class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_quantity = 0
        current_quantity = 0

        for index in range(len(s)):
            if s[index] in vowels:
                current_quantity += 1
            if index >= k:
                if s[index - k] in vowels:
                    current_quantity -= 1
            max_quantity = max(max_quantity, current_quantity)
        return max_quantity
