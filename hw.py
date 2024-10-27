from collections import defaultdict

# Набір монет
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    result = defaultdict(int)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    return dict(result)

def find_min_coins(amount):
    # Таблиця для збереження мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 потрібно 0 монет

    # Таблиця для збереження кількості монет для кожного номіналу
    coin_count = [defaultdict(int) for _ in range(amount + 1)]

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if current_amount >= coin:
                remaining_amount = current_amount - coin
                if min_coins[remaining_amount] + 1 < min_coins[current_amount]:
                    min_coins[current_amount] = min_coins[remaining_amount] + 1
                    coin_count[current_amount] = coin_count[remaining_amount].copy()
                    coin_count[current_amount][coin] += 1

    return dict(coin_count[amount])

# Приклади використання:
amount = 113

# Використання жадібного алгоритму
greedy_result = find_coins_greedy(amount)
print(f"Жадібний алгоритм (сума {amount}): {greedy_result}")

# Використання динамічного програмування
dp_result = find_min_coins(amount)
print(f"Динамічне програмування (сума {amount}): {dp_result}")
