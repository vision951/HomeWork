import os

import pytest

from src.decorators import log


@log()
def successful_function(x, y):
    return x + y


@log()
def failing_function(x, y):
    raise ValueError("Something went wrong")


@log(filename="test_log.txt")
def successful_function_with_file(x, y):
    return x + y


@log(filename="test_log.txt")
def failing_function_with_file(x, y):
    raise TypeError("Type error occurred")



def test_successful_function(capsys):
    """Проверка успешного выполнения функции с логированием в консоль"""
    successful_function(2, 3)
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')
    assert len(output) == 2
    assert output[0].endswith("successful_function: Starting")
    assert output[1].endswith("successful_function: ok")


def test_failing_function(capsys):
    """Проверка обработки ошибки с логированием в консоль"""
    with pytest.raises(ValueError):
        failing_function(2, "three")
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert "failing_function: Starting" in output
    assert "failing_function: error: ValueError. Inputs: (2, 'three'), {}" in output


def test_successful_function_with_file():
    """Проверка успешного выполнения с логированием в файл"""
    # Очищаем файл перед тестом
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    successful_function_with_file(4, 5)
    with open("test_log.txt", "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip().endswith("successful_function_with_file: Starting")
        assert lines[1].strip().endswith("successful_function_with_file: ok")


def test_failing_function_with_file():
    """Проверка обработки ошибки с логированием в файл"""
    # Очищаем файл перед тестом
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    with pytest.raises(TypeError):
        failing_function_with_file(4, "five")
    with open("test_log.txt", "r") as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip().endswith("failing_function_with_file: Starting")
        assert lines[1].strip().endswith("failing_function_with_file: error: TypeError. Inputs: (4, 'five'), {}")


def test_decorator_with_no_arguments(capsys):
    """Проверка работы декоратора без аргументов"""

    @log()
    def simple_function():
        return "Hello"

    assert simple_function() == "Hello"
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')
    assert len(output) == 2
    assert output[0].endswith("simple_function: Starting")
    assert output[1].endswith("simple_function: ok")
