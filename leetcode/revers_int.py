class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        string = str(abs(x))
        rev_string = string[::-1]
        res =  int(rev_string) if not neg else int(rev_string)*-1
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        else:
            return res

if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))
    x = -120
    print(Solution().reverse(x))
    print("--"*20)
    x = 1534236469
    print(f"o: {(2**31)-1}")
    print(f"x: {x}")

    print(Solution().reverse(x))