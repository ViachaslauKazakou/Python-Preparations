from typing import List
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        string = str(abs(x))
        rev_string = string[::-1]
        res = int(rev_string) if not neg else int(rev_string)*-1
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        else:
            return res

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        print(f"String before: {s}")
        s_len = len(s)
        for i in range(int(s_len/2)):
            s_curr = s[i]
            s[i] = s[s_len-i-1]
            s[s_len - i - 1] = s_curr
        print(f"String after: {s}")



if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))
    x = -120
    print(Solution().reverse(x))
    print("--" * 40)
    x = 153423646
    print(f"o: {(2**31)-1}")
    print(f"x: {x}")

    print(Solution().reverse(x))
    s = ["A", "b", "c", "E", "d"]
    Solution().reverseString(s)
