import re

class WordIterable:
    def __init__(self, text):
        self.text = re.findall(r'[a-zA-ZА-Яа-я]+', text)
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num += 1
        if self.current_num > len(self.text):
            raise StopIteration()
        return self.text[self.current_num -1]

if __name__ == '__main__':
    text = 'мама. мыла? раму!'
    text2 = 'Я. был.. слишком. беспечен'
    test1 = 'VHbJndc.! nvfjks. bfaghh?  fbdja...'
    test2 = 'cvgvdshr4@ nvna444fkjg  hahhk? bbb4'
    for i in WordIterable(text):
        print(i)
    for w in WordIterable(text2):
        print(w)
    for i in WordIterable(test1):
        print(i)
    for i in WordIterable(test2):
        print(i)