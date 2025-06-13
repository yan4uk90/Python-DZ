import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Тест 1: Тестирование функциональности "capitalize"
@pytest.mark.parametrize("string, result", [
    # Позитивные проверки:
    ("skypro", "Skypro"),
    ("skyPro", "Skypro"),
    ("hello world", "Hello world"),
    ("dr'house", "Dr'house"),
    ("yana1", "Yana1"),
    # Негативные проверки:
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("OMP", "Omp")
])
def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result


# Тест 2: Тестирование функциональности "trim"
@pytest.mark.parametrize('string, result', [
    # Позитивные проверки:
    (" abc", "abc"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),
    ("   Yana1", "Yana1"),
    # Негативные проверки:
    ("", ""),
    ("and rey", "and rey"),
    ("cola", "cola"),
    ("123  ", "123  ")
])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result


# Тест 3: Тестирование функциональности "contains"
@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("Yana", "a", True),
    (" west", "t", True),
    ("ice  ", "e", True),
    ("Sobaka-Ulybaka", "-", True),
    ("123", "1", True),
    ("", "", True),
    # Негативные проверки:
    ("Yana", "x", False),
    ("hello", "!", False),
    ("", "x", False),
    ("hello", "xyz", False)
])
def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result


# Тест 4: Тестирование функциональности "delete_symbol"
@pytest.mark.parametrize('string, symbol, result', [
    # Позитивные проверки:
    ("screem", "s", "creem"),
    ("Woland", "o", "Wland"),
    ("West", "t", "Wes"),
    ("12345", "1", "2345"),
    ("Sobaka-Ulybaka", "-", "SobakaUlybaka"),
    # Негативные проверки:
    ("Yana", "k", "Yana"),
    ("", "", ""),
    ("", "g", ""),
    ("milk", "", "milk"),
    ("carpet  ", "r", "capet  ")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result
