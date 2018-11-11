"""
ジェネレーター send の使い方、いまいちぱっとこないなあ
"""
import sys

#def raw_input(input):
#    return input

def upper_input(input):
    return input.upper()

def echo_handler():
    while True:
        data = yield upper_input(input())
        yield sys.stdout.write('stdout: %s\n' % data)


def main():
    g = echo_handler()
    r = None
    while True:
        print('Before send(): ', r)
        r = g.send(r)
        print('After send(): ', r)
        print('-' * 20)

if __name__ == '__main__':
    main()

