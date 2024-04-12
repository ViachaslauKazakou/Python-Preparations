class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        
if __name__ == "__main__":
    haystack = "qsawdbutsad"
    needle = "sad"
    print(Solution().strStr(haystack, needle))