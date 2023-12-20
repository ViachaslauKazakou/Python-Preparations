es = "()[]{}"
class Braket:
    validator = {
        '(':')',
        '[':']',
        '{':'}'
    }

class Solution(object):
    validator = {
        '(':')',
        '[':']',
        '{':'}'
    }
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check_list = list(s)
        if check_list[0] in ')]}':
            return False
        else:
            for key, item in enumerate(check_list):
                print(f"{key}:{item}")
                print(self.validator[item])
            return True

s = "(}{{}{}}"

print(Solution().isValid(s))
