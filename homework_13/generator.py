def generate_words(text: str):
    new_text = text.split()
    for i in new_text:
        yield i


if __name__ == '__main__':
    text = 'мама мыла раму'
    for i in generate_words(text):
        print(i)