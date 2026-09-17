class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s
        word = word.strip()
        splitter = word.split(" ")
        last_word = splitter[-1]
        word_lenght = len(last_word)
        return word_lenght