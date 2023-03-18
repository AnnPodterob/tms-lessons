def get_longest_world(text: str):
    f = (text.split())
    pos = 0
    maxs = len(f[pos])
    for i in range(len(f)):
        if len(f[i]) > maxs:
            maxs = len(f[i])
            pos = i
    return f[pos]

print(get_longest_world("hello this is a string with words and spaces and big big woooooooooord"))
