# 課題制作中

# users_info を使って出力する…ネストされたリストから要素を取り出す

users_info = [
    ["Bob", 79],
    ["Tom", 59],
    ["Ken", 61]
    ]

print(f"Name: {users_info[0][0]}, Age: {users_info[0][1]}")  # 親リスト1番目の中の子リストの1番目、親リスト1番目の中の子リストの2番目
print(f"Name: {users_info[1][0]}, Age: {users_info[1][1]}")  # 親リスト2番目の中の子リストの1番目、親リスト2番目の中の子リストの2番目
print(f"Name: {users_info[2][0]}, Age: {users_info[2][1]}")  # 親リスト3番目の中の子リストの1番目、親リスト3番目の中の子リストの2番目
