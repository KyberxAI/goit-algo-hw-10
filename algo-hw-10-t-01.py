import timeit


def find_coins_greedy(amount: int) -> dict:
    """
    Жадібний алгоритм для видачі решти.
    Спочатку вибирає найбільші доступні номінали монет.
    """
    COINS_LIST = [50, 25, 10, 5, 2, 1]
    result = {}
    # Для кожного номіналу монет отримуэмо цілу частину від ділення,
    # на наступну ітерацію передаємо залишок
    for coin in COINS_LIST:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin
    return result


def find_min_coins(amount: int) -> dict:
    """
    Алгоритм динамічного програмування для знаходження
    мінімальної кількості монет для заданої суми.
    """
    COINS_LIST = [50, 25, 10, 5, 2, 1]
    n = len(COINS_LIST)

    # Створюємо таблицю для мінімальної кількості монет
    K = [[float('inf') for w in range(amount + 1)] for i in range(n + 1)]

    # Заповнюємо таблицю знизу вгору
    for i in range(n + 1):
        for w in range(amount + 1):
            if w == 0:
                K[i][w] = 0
            elif i == 0:
                K[i][w] = float('inf')
            elif COINS_LIST[i - 1] <= w:
                K[i][w] = min(1 + K[i][w - COINS_LIST[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Відновлюємо набір монет
    result = {}
    i = n
    w = amount

    while w > 0:
        if K[i][w] == K[i - 1][w]:
            i -= 1
        else:
            coin = COINS_LIST[i - 1]

            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1

            w -= coin

    return result


# Приклад використання:
if __name__ == "__main__":
    amounts = [13, 193, 1093, 10093, 100093, 1000093]
    runs = 3

    print("| Сума    |  Жадібний, с | Динамічний, с| Кратність, х | Результати алгоритмів Ж і Д                     |")
    print("|---------|--------------|--------------|--------------|-------------------------------------------------|")
    for amount in amounts:
        time_greedy_alg = timeit.timeit(
            lambda: find_coins_greedy(amount), number=runs) / runs
        time_dynamic_alg = timeit.timeit(
            lambda: find_min_coins(amount), number=runs) / runs

        ratio = max(time_greedy_alg, time_dynamic_alg) / min(
            time_greedy_alg, time_dynamic_alg)

        result_greedy = find_coins_greedy(amount)
        result_dynamic = dict(
            sorted(find_min_coins(amount).items(), reverse=True))

        print(
            f"|{amount:>8} | {time_greedy_alg:>12.8f} | {time_dynamic_alg:>12.8f} |{ratio:>12.1f}x |   {'':>45} |"
            f"\n|{'':>8} | {'':>12} | {'':>12} | {'':>12} | Ж: {str(result_greedy):<45}|"
            f"\n|{'':>8} | {'':>12} | {'':>12} | {'':>12} | Д: {str(result_dynamic):<45}|"
        )
