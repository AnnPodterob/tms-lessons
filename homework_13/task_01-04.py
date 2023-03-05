import re

def is_date(s: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', s) is not None


def is_float_number(s: str) -> bool:
    return re.fullmatch(r'\b[+-]?\d+\.\d+\b', s) is not None


class WordIterable:
    def __init__(self, text):
        self.text = text.split()
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num += 1
        if self.current_num > len(self.text):
            raise StopIteration()
        return self.text[self.current_num -1]

if __name__ == '__main__':
    text = 'мама мыла раму'
    text2 = 'Я был слишком беспечен'
    for i in WordIterable(text):
        print(i)
    for w in WordIterable(text2):
        print(w)
