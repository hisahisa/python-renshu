def accumulate():
    tally = 0
    while 1:
        nex = yield
        if nex is None:
            return tally
        tally += nex


def gather_tallies(tallies):
    while 1:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []
ac = gather_tallies(tallies)

print("1")
print(next(ac))

print("2")
print(ac.send(5))



