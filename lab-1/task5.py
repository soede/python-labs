import re


def find_dates(text):
    pattern = r"\b(0?[1-9]|[12][0-9]|3[01]) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) \d{4}\b"

    matches = re.findall(pattern, text)
    dates = [" ".join(match) for match in matches]
    return dates


text = input()
print(find_dates(text))
