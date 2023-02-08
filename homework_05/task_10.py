# Напишите функцию get_most_frequent_word, которая на вход
# принимает текст (только английские слова и пробелы),
# и возвращает самое часто встречающееся слово.
# Если таких слов несколько - верните любое.

def get_most_frequent_word(text: str):
    counter = {}
    for i in text:
        line = text.split()
        for word in line:
            counter[word] = counter.get(word, 0) + 1
    max_count = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_count]
    return min(most_frequent)

print(get_most_frequent_word('bdh vip vip vip in in in dK'))