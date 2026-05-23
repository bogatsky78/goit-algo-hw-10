COINS = [50, 25, 10, 5, 2, 1]

# Greedy algorithm to find coins
def find_coins_greedy(amount: int) -> dict:
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Dynamic programming algorithm to find minimum coins
def find_min_coins(amount: int) -> dict:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result[coin] = result.get(coin, 0) + 1
        remaining -= coin

    return dict(sorted(result.items()))


if __name__ == "__main__":
    import time

    test_amounts = [113, 1000, 10_000, 100_000]

    for amount in test_amounts:
        print(f"\nAmount: {amount}")

        start = time.perf_counter()
        greedy_result = find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start
        print(f"  Greedy : {greedy_result}  ({greedy_time:.6f}s)")

        start = time.perf_counter()
        dp_result = find_min_coins(amount)
        dp_time = time.perf_counter() - start
        print(f"  DP     : {dp_result}  ({dp_time:.6f}s)")
