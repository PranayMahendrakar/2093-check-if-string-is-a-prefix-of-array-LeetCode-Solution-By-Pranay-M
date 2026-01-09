class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concat = ""
        for word in words:
            concat += word
            if concat == s:
                return True
            if len(concat) > len(s):
                return False
        return False