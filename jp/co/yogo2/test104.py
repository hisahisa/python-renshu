en = [70, 50, 80, 50, 90]
ma = [20, 70, 40, 90, 30]
cov = lambda item1, item2: \
    sum([(i[0]-sum(item1)/len(item1)) * (i[1]-sum(item2)/len(item2)) for i in zip(item1, item2)]) \
    / len(item1)

print(cov(en,ma))
