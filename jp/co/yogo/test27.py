import os
import threading

MAX_COUNT = 10000000
ITERATION = 5000000


def whoami(what):
    # 単純な加算
    count = 1
    for n in range(MAX_COUNT):
        if count % ITERATION == 0:
            # 実行中のプロセスIDと,現在のcount数とスレッドナンバーを表示
            print("{} Process {} thread= {} count {}".format(what, os.getpid(), threading.current_thread(), count))
        count += 1
    # どのスレッドが終了したかを表示
    print("end {} Thread {}".format(what, threading.current_thread()))


# 現在のプロセスのidを表示
print("Main Process ID is {}".format(os.getpid()))
# メインのプロセスで実行
whoami("main program")

for n in range(10):
    p = threading.Thread(target=whoami, args=("Thread {}".format(n),))
    p.start()
print("end of program")
