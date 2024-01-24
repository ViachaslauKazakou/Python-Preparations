class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = []
        for key, item in enumerate(strs[0]):
            check = True
            for i in strs:
                try:
                    if item != i[key]:
                        check = False
                except:
                    check = False
                    break
            if check:
               res.append(item)
            else:
                break
        return "".join(res)



if __name__ == "__main__":
    strs = ["flower", "flow", "flight", "flode", "florer"]
    # strs = ["ab", "a"]
    res = Solution()
    print(f"res : {res.longestCommonPrefix(strs)}")