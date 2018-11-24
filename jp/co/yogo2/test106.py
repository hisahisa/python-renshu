
def gen_etos():
    ETOS = '子丑寅卯辰巳午未申酉戌亥'
    for eto in ETOS:
        s = 'moji'
        yield eto + s



g1 = gen_etos()

# ジェネレータ関数の戻り値はジェネレータオブジェクト
type(g1)
# => generator

# ジェネレータかどうかのチェックは types の GeneratorType でできる
import types
print(isinstance(g1, types.GeneratorType))

#for g in g1:
#    print(g)

try:
    while True:
        print(next(g1))
except StopIteration:
    print("ループ終了")






