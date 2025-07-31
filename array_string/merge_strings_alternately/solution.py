class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for index in range(max(len(word1), len(word2))):
            if index < len(word1):
                result.append(word1[index])
            if index < len(word2):
                result.append(word2[index])

        return "".join(result)
