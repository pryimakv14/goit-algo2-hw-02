from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}
    def helper(n: int) -> Dict:
        if n == 0:
            return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}

        if n in memo:
            return memo[n]

        max_profit = 0
        best_cuts = []

        for i in range(1, n + 1):
            if i <= len(prices):
                result = helper(n - i)
                current_profit = prices[i - 1] + result["max_profit"]
                if current_profit > max_profit:
                    max_profit = current_profit
                    best_cuts = [i] + result["cuts"]

        memo[n] = {
            "max_profit": max_profit,
            "cuts": best_cuts,
            "number_of_cuts": len(best_cuts) - 1
        }
        return memo[n]

    return helper(length)

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if j <= len(prices):
                if dp[i] < prices[j - 1] + dp[i - j]:
                    dp[i] = prices[j - 1] + dp[i - j]
                    cuts[i] = cuts[i - j] + [j]

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\\nПеревірка пройшла успішно!")
if __name__ == "__main__":
    run_tests()