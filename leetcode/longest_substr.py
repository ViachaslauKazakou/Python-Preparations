class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        charstr = []
        max_ls = 1
        for i in range(0,len(s)):
            if s[i] not in charstr:
                charstr.append(s[i])
                if len(charstr) > max_ls:
                    max_ls = len(charstr)
            else:
                charstr = [s[i]]
        return max_ls
        
if __name__ == "__main__":
    # s = "dvdf"
    # print(Solution().lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))