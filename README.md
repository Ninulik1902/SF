# Проект SF. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Код-решение](.README.md#код-решение)  
[6. Результат](.README.md#Результат)    
[7. Выводы](.README.md#Выводы)

### Описание проекта    
Проект заключается в создании программы, которая будет угадывать загаданное компьютером число за минимальное количество попыток.

:arrow_up:[к оглавлению](_)

### Какой кейс решаем?    
Мы решаем задачу угадывания числа, загаданного компьютером, с использованием эффективных алгоритмов.

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и задача угадать это число с использованием алгоритма.
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**    
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

**Что практикуем**    
В процессе решения этой задачи мы практикуем навыки написания эффективного кода на Python.

:arrow_up:[к оглавлению](.README.md#Оглавление)

### Краткая информация о данных
В данном проекте данные не используются, так как основной задачей является разработка алгоритма угадывания числа.

:arrow_up:[к оглавлению](.README.md#Оглавление)

### Этапы работы над проектом  
1. Разработка простого алгоритма случайного угадывания.
2. Создание алгоритма угадывания с коррекцией на основе полученной информации.
3. Реализация более эффективного алгоритма угадывания.

:arrow_up:[к оглавлению](.README.md#Оглавление)

### Код решения

```python
def game_core_v3(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 1
    low_limit, high_limit = 1, 100
    predict = 50  # начинаем с середины диапазона
    while number != predict:
        count += 1
        if number > predict:
            low_limit = predict + 1
        else:
            high_limit = predict - 1
        predict = (low_limit + high_limit) // 2  # берем середину нового диапазона
    return count
```

:arrow_up:[к оглавлению](.README.md#Оглавление)

#### Результат:  
На текущий момент результаты оценки эффективности алгоритмов следующие:
- Алгоритм случайного угадывания: среднее количество попыток - X.
- Алгоритм угадывания с коррекцией: среднее количество попыток - Y.
- Эффективный алгоритм (ваш вариант): среднее количество попыток - Z.

:arrow_up:[к оглавлению](.README.md#Оглавление)
