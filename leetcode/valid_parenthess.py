from dataclasses import dataclass

es = "()[]{}"


class Braket:
    validator = {"(": ")", "[": "]", "{": "}"}


@dataclass
class Solution(object):
    s: int = None

    validator = {"(": ")", "[": "]", "{": "}"}

    def _isValid(self):
        """
        :type s: str
        :rtype: bool
        """
        check_list = list(self.s)
        valid = False
        if check_list[0] in ")]}":
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

    def isValid(self):
        check_list = list(self.s)
        print(check_list)


if __name__ == "__main__":
    s = ["{[}]", "[{}]", "[{]"]
    for item in s:
        print("=" * 80)
        print(f"check: {item}")
        print(Solution(item).isValid())
