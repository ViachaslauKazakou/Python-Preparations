es = "()[]{}"
class Braket:
    validator = {
        '(':')',
        '[':']',
        '{':'}'
    }

class Solution(object):
    validator = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check_list = list(s)
        valid = False
        if check_list[0] in ')]}':
            return valid
        while len(check_list) > 0:
            print(check_list)
            print(check_list[0])
            find_el = self.validator.get(check_list[0])
            if find_el and find_el in check_list:
                valid = True
                check_list.remove(find_el)
                check_list.pop(0)
            else:
                valid = False
                return valid
        return valid






if __name__ == "__main__":

    s = "{[}]"

    print(Solution().isValid(s))
    s = "[{}]"

    print(Solution().isValid(s))

    s = "[{]"
    print(Solution().isValid(s))