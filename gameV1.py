def game_core_v3(number: int = 1) -> int:
    """
    Функция для угадывания числа бинарным поиском.

    Args:
        number (int, optional): Загаданное число. По умолчанию 1.

    Returns:
        int: Число попыток, необходимых для угадывания числа.
    """
    count = 1  # Начинаем считать попытки с 1

    left = 1
    right = 100
    while True:
        predict = (left + right) // 2
        if predict == number:
            break
        elif predict < number:
            left = predict + 1
        else:
            right = predict - 1
        count += 1

    return count

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
