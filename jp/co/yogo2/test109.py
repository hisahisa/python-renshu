
import numpy as np
import matplotlib.pyplot as plt

#関数、積分範囲の定義
def f(x): return np.log(np.log(x))
a=3
b=10

#刻み幅と短冊の各々のx座標
N=1000
x=np.linspace(a,b,N)

#面積（始めは0でどんどん足していく）
S=0

#積分処理
for i in range(len(x)-1):
    y=(f(x[i])+f(x[i+1]))/2
    S+=(x[i+1]-x[i])*y #小さい短冊を足しあげる

print(S) #結果表示