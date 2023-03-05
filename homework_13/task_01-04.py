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
    assert is_date('12-12-1999')
    assert not is_date('123-23-1999')
    assert is_float_number('234.542')
    assert is_float_number('23.3')
    assert not is_float_number('341342,432')
    assert not is_float_number('65473')
    text = 'мама мыла раму'
    text2 = 'Я был слишком беспечен'
    for i in WordIterable(text):
        print(i)
    for w in WordIterable(text2):
        print(w)
