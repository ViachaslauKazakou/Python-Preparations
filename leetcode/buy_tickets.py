from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    counter += 1
                if tickets[k] == 0 and tickets[i] == tickets[k]:
                    return counter 
                if tickets[k] == 0:
                    return counter 

                    
        return counter
                
if __name__ == "__main__":
    tickets = [2,3,2]
    k = 2
    res = Solution().timeRequiredToBuy(tickets, k)
    print(f"Result time: {res}")
    tickets = [5,1,1,1]
    k = 0
    res = Solution().timeRequiredToBuy(tickets, k)     
    print(f"Result time: {res}")       