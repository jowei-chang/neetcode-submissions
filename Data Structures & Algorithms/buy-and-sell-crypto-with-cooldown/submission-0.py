class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_wo, stock_w, colddown = 0, -prices[0], 0

        for nn in prices[1:]:
            stock_w = max(stock_w, colddown-nn)
            colddown = max(colddown, stock_wo)
            stock_wo = max(stock_wo, stock_w+nn)
        return stock_wo