def is_year_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_year_leap(1998))
print(is_year_leap(2024))
print(is_year_leap(200))