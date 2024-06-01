class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max:
                max = price - min_price

        return max
