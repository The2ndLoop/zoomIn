from hashids import Hashids

# 作るハッシュidの桁数
digits = 4

# 作るハッシュidの数
hash_num = 200

print()
name = input('作りたいファイルの名前を入力してください->')
print()

# hashidsインスタンスを作成
hashids = Hashids(
    salt=name, min_length=digits
)


try:

    # 例外発生
    if "/" in name:
        raise ValueError("/")
    elif "." in name:
        raise ValueError(".")

    # ファイルオープン
    with open("./_rooms/" + name + ".txt", 'w', encoding="utf-8") as f:

        # 重複を確認する用
        hash_lst = []

        # ファイルに書き込み
        for num in range(1,hash_num+1):

            id = hashids.encode(num)

            hash_lst.append(id)

            hash_id = id + "\n"

            f.write(hash_id)

    # 成功かどうか判定
    if len(hash_lst) == len(set(hash_lst)):
        print("成功しました")
        print()
    else:
        print("失敗しました")
        print("重複が出ました")

# 例外処理
except ValueError as e:
    print('"' + str(e) + '"' + "をファイル名に使わないでください")
    print()

# except FileNotFoundError:
#     print("失敗しました。")
#     print()
#     print("このファイルを置く位置が違います。")
#     print()
#     print("oTreeのプロジェクトフォルダ直下においてください。")
#     print()
#     print("settings.pyとかがあるフォルダです。")
#     print()






