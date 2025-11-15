from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_counter = Counter(word1)
        word2_counter = Counter(word2)

        return (
            sorted(word1_counter.values()) == sorted(word2_counter.values())
            and word2_counter.keys() == word2_counter.keys()
        )


print(Solution().closeStrings(word1="abc", word2="bca"))
print(Solution().closeStrings(word1="a", word2="aa"))
print(Solution().closeStrings(word1="cabbba", word2="abbccc"))
