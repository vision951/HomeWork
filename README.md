# Банкровские транзакции

## Описание проекта
Проект предоставляет набор функций для обработки списка банковских транзакций:
- Фильтрация по статусу
- Сортировка по дате
- Маскировка номеров карт и счетов
- Форматирование дат


## Установка

1. Склонируйте репозиторий:
   ```
   git clone git@github.com:vision951/HomeWork.git
2. Установка зависимостей
    ```
   poetry install
3. Активация виртуального окружения:
    ```
   poetry shell
4. Установка линтеров flake8, mypy, black, isort
   ```
   poetry add flake8 --group lint
   poetry add mypy --group lint
   poetry add black --group lint
   poetry add isort --group lint

##  Проверки и тестирование

Проект проходит следующие виды проверок:

### 1. Статическая проверка типов (mypy)
      ```
      poetry run mypy src/
### 2. Проверка стилея(flake8)
      ```
      poetry run flake8 src/

## Примеры работы функций
### Фильтрация выполненных транзакций
executed = filter_by_state(transactions, state="EXECUTED")

### Сортировка по дате (новые сначала)
- sorted_transactions = sort_by_date(transactions)

### Маскировка карты → "Visa Platinum 1234 56** **** 3456"
masked_card = mask_number("Visa Platinum 1234567890123456") 

### Маскировка счета → "Счет **3456"
account_masked = mask_number("Счет 1234567890123456")

### Форматирование даты → 1.03.2024
formatted_date = get_date("2024-03-11T02:26:18.671407")