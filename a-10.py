# 課題提出中

"""
下記のコードが期待通り動作するような、dice() 関数を実装する
※ dice()関数は1から6の整数をランダムに返す
print(dice()) # 1から6の整数をランダムに出力する
"""


import random                     # randomモジュールをインポートする


def dice():                       # dice関数を定義する
    return random.randint(1, 6)   # dice関数は1から6までの範囲から1つをランダムに返す


print(dice())                     # 1から6の整数をランダムに出力する
