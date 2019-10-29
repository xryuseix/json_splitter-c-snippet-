# C++スニペットを分割する
# 分割したら同フォルダ内に分割したcppファイルとして保存
# 行数が３行未満のスニペットは無視
# includeとかは放置

import json

# jsonを辞書に変更
file = open('./sample.json', 'r')
json_dict = json.load(file)

# print(json_dict['baz']['foo'])

keys = json_dict.keys()

print(keys)

for k in keys:
    file_pass = './' + k + '.cpp'
    print(file_pass)
    #書き込むファイルを開く
    file_write = open(file_pass, 'w')
    json.dump(json_dict[k], file_write)