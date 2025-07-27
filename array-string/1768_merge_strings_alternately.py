class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for index in range(max(len(word1), len(word2))):
            if index < len(word1):
                result.append(word1[index])
            if index < len(word2):
                result.append(word2[index])

        return ''.join(result)

assert Solution().mergeAlternately(word1="abc", word2="pqr") == "apbqcr", "Test 1 Failed"
assert Solution().mergeAlternately(word1="ab", word2="pqrs") == "apbqrs", "Test 2 Failed"
assert Solution().mergeAlternately(word1="abcd", word2="pq") == "apbqcd", "Test 3 Failed"
