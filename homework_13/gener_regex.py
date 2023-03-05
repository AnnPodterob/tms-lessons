import re

def generate_words(text: str):
    new_text = re.findall(r'[a-zA-ZА-Яа-я]+', text)
    for i in new_text:
        yield i


if __name__ == '__main__':
    text = 'мама. мыла? раму!'
    text2 = 'Я. был.. слишком. беспечен'
    test1 = 'VHbJndc.! nvfjks. bfaghh?  fbdja...'
    test2 = 'cvgvdshr4@ nvna444fkjg  hahhk? bbb4'
    for i in generate_words(text):
        print(i)
    for w in generate_words(text2):
        print(w)
    for i in generate_words(test1):
        print(i)
    for i in generate_words(test2):
        print(i)