# 課題提出中

# membersというリストから "Bob" と "Tom" を取得して出力する
members = ["Bob", "Tom", "Ken"]


print(f"① membersリストから、{members[:2]}を取得して出力しました。")
print(f"'① または、membersリストから、{members[0]} と {members[1]} を取得して出力しました。")

print("")  #改行


# membersというリストから "Bob" と "Tom" を取得して、それぞれ1件ずつ"Bob" と "Tom"を出力する
members2 = (members[:2])    # スライスしたリストを変数に代入する


print(f"②-1 menbersリストから'Bob' と 'Tom' を取得後、{members2[0]} を出力しました。")
print(f"②-2 menbersリストから'Bob' と 'Tom' を取得後、{members2[1]} を出力しました。")

print("")  #改行
