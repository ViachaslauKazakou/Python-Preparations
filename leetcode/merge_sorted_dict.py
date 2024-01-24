class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = []
        res.extend(list1)
        res.extend(list2)
        return sorted(res)


if __name__ == "__main__":
    list1 = [0]
    list2 = []
    res = Solution()
    print(res.mergeTwoLists(list1, list2))
