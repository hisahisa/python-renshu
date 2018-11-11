#改行を除く
with open('/Users/yogohisashi/yogodev/testyogo1.txt') as f:
    for line in f:
        if (len(line) - line.count('\n')) <= 0:
            continue
        x = dict([line.split(None)])
        print(x)
