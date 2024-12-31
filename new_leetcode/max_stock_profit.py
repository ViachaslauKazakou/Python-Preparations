prices = [7,1,5,3,6,4]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        benefit = 0
        stock = 0
        start = prices[0]
        print(prices)
        for curr in range(1, len(prices)):
            print(f"Current price: {prices[curr]}, byued stocks: {stock}")
            if prices[curr]< start: # buy
                benefit = prices[curr]
                stock = 1
                print(f"Buy stock. buied: {prices[curr]}")
            elif prices[curr] > prices[curr-1] and stock: # sell 
                stock = 0
                benefit = benefit + prices[curr]
                print(f"Sell stock.  sold: ")
            start = prices[curr]
                
        print(f"Benefith: {benefit}")
                
                
if __name__ == "__main__":
    
    Solution().maxProfit(
        prices
    )
    
    
                 