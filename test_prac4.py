from prac4 import normalize_phone_in_line


def test_russian_plus7_number():
    assert normalize_phone_in_line("+7 (900) 123-45-67") == "+1 (900) 1234567"


def test_russian_8_number():
    assert normalize_phone_in_line("8 912 345 67 89") == "+1 (912) 3456789"


def test_short_number_10_digits():
    assert normalize_phone_in_line("(921)3334455") == "+1 (921) 3334455"


def test_international_number_with_extra_digits():
    assert normalize_phone_in_line("+380 50 123 4567") == "+1 (050) 1234567"


