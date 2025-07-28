class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1, length2 = len(str1), len(str2)

        def is_valid_gcd(index):
            if length1 % index or length2 % index:
                return False
            n1, n2 = length1 // index, length2 // index
            base = str1[:index]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(length1, length2), 0, -1):
            if is_valid_gcd(i):
                return str1[:i]
        return ""