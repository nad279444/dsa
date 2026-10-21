"""Maximum profit from buying and selling stock, with one or two trades.

buy_and_sell_shares: one forward pass that tracks the cheapest price seen so
far. For each day the best profit ending that day is `price - min_price`, and
the answer is the max of those (0 if the price never rises).
Time O(n), Space O(1).

buy_and_sell_stock_twice: a forward pass records in `first_buy_sell_profits[i]`
the best single-trade profit achievable using only days 0..i. A backward pass
then tracks the highest price seen ahead, combining "best trade completed before
day i" with "buy on day i and sell at the future max price", keeping the overall
maximum. The two trades never overlap because the sell of trade 1 is at i - 1.
Time O(n), Space O(n).
"""

# write a program that takes an array denoting the daily stock price, and returns the maximum profit
# that could be made by buying and selling one share of the stock


def buy_and_sell_shares(prices: list[int]):
    max_profit = 0
    min_price = float("inf")

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


# write a program that computes the maximum profit
# that can be made by buying and selling a share at most twice
# The second buy must be made on another date after the first sale


def buy_and_sell_stock_twice(prices: list[int]):
    max_total_profit, min_price = 0.0, float("inf")
    first_buy_sell_profits = [0.0] * len(prices)

    for i, price in enumerate(prices):
        min_price = min(min_price, price)
        max_total_profit = max(max_total_profit, price - min_price)
        first_buy_sell_profits[i] = max_total_profit

    max_price = float("-inf")
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, price)
        max_total_profit = max(
            max_total_profit, max_price - price + first_buy_sell_profits[i - 1]
        )
    return max_total_profit


if __name__ == "__main__":
    # One trade: buy at 260 and sell at 300 -> profit 40
    assert buy_and_sell_shares([310, 315, 275, 295, 260, 300, 277, 292, 240, 260]) == 40

    # Prices never rise -> no profitable trade -> 0
    assert buy_and_sell_shares([310, 310, 275, 275, 260, 260, 260, 230, 230, 230]) == 0

    # Single day -> nothing to sell -> 0
    assert buy_and_sell_shares([5]) == 0

    # Two trades: 275 -> 315 (40) plus 240 -> 260 (20) -> 60
    assert buy_and_sell_stock_twice([310, 315, 275, 295, 260, 300, 277, 292, 240, 260]) == 60

    # Two trades: 1 -> 5 (4) plus 3 -> 6 (3) -> 7
    assert buy_and_sell_stock_twice([1, 5, 3, 6, 4]) == 7

    # Two trades: 2 -> 5 (3) plus 0 -> 8 (8) -> 11
    assert buy_and_sell_stock_twice([2, 5, 0, 8, 2]) == 11

    print("All tests passed")
