def front_x(words):
    a = []
    for i in words:
        if i[0] == 'x':
            a.append(i)
            words.remove(i)
    a.sort()
    words.sort()
    return a + words