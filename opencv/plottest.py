# ２次元リアルタイムグラフの雛形

# Library
import numpy as np # プロットするデータ配列を作成するため
import matplotlib.pyplot as plt # グラフ作成のため

# params
dataLength = 100  # １つのデータの配列の点数
frame = 50  # プロットするフレーム数
sleepTime = 0.0001  # １フレーム表示する時間[s]

# plotting
for i in range(frame): # フレーム回数分グラフを更新
    data = np.random.rand(dataLength) # プロットするデータを作成
    plt.plot(data) # データをプロット
    plt.draw() # グラフを画面に表示開始
    plt.pause(sleepTime) # SleepTime時間だけ表示を継続
    plt.cla() # プロットした点を消してグラフを初期化