class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')

        result = list(s)

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and result[left_pointer].lower() not in vowels:
                left_pointer += 1
            while left_pointer < right_pointer and result[right_pointer].lower() not in vowels:
                right_pointer -= 1

            result[left_pointer], result[right_pointer] = result[right_pointer], result[left_pointer]
            left_pointer += 1
            right_pointer -= 1

        return ''.join(result)