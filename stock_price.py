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
    print(buy_and_sell_shares([310, 310, 275, 275, 260, 260, 260, 230, 230, 230]))
