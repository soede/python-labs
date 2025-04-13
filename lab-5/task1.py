import re

def is_mail_zip(s: str) -> bool:
    return bool(re.fullmatch(r'\d{6}', s))

def get_zip_code(s: str) -> str:
    if is_mail_zip(s):
        return s
    else:
        raise ValueError(f"Некорректный почтовый индекс: {s}")

try:
    print(is_mail_zip("12345"))  # True
    print(get_zip_code("12345"))  # 12345
    print(get_zip_code("12a45"))  # Ошибка
except ValueError as e:
    print(e)
