import urllib.request

# Переменная содержит запрос к 'http://localhost:1234/'.

fp = urllib.request.urlopen("http://localhost:1234/")

# 'encodedContent' соответствует закодированному ответу сервера ('index.html').
# 'decodedContent' соответствует раскодированному ответу сервера (тут будет то, что мы хотим вывести на экран).

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")


print(decodedContent)