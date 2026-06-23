class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        l=0
        r=l+1
        while l< len(prices)-1:
            if prices[r]< prices[l]:
                l=r
                r=l+1
            else:
                p = prices[r] - prices[l]
                max_price = max(max_price, p)
                if r == len(prices)-1:
                    l=l+1
                    r=l+1
                else:
                    r = r +1
        return max_price