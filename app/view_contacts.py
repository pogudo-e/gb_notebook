def view(file_contents):
    ''' Show full contact list '''
    res = ''
    if len(file_contents) == 0:
        res = "Ой, кажется тут пусто :("
    else:
        print()
        for i in range(0, len(file_contents)):
            for i2 in range(0, len(file_contents[i])):
                res += file_contents[i][i2] + ' '
            res += '\n'
    return res