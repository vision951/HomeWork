from datetime import datetime
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Фиксируем начало
            time_stamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            # Логируем начало выполнения
            log_message(f"[{time_stamp}] {func.__name__}: Starting", filename)

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)
                # Фисируем окончание
                time_stamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
                # Логируем конец выполнения
                log_message(f"[{time_stamp}] {func.__name__}: ok", filename)
                return result
            except Exception as e:
                # Фисируем окончание
                time_stamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
                error_type = type(e).__name__
                # Логируем конец выполнения с ошибкой
                log_message(f"[{time_stamp}] {func.__name__}: error: {error_type}. Inputs: {args}, {kwargs}", filename)
                raise
        return wrapper
    return decorator


def log_message(message, filename=None):
    """ Записывает сообщение в файл или выводит в консоль."""
    if filename:
        with open(filename, 'a') as f:
            f.write(message + '\n')
    else:
        print(message)
