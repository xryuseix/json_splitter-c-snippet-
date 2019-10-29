# C++スニペットを分割する
# 分割したら同フォルダ内に分割したcppファイルとして保存
# 行数が３行未満のスニペットは無視
# includeとかは放置

import json

# jsonを辞書に変更
file = open('./c++snippet.json', 'r')
json_dict = json.load(file)

keys = json_dict.keys()

for k in keys:
    file_pass = './snippets/' + k + '.cpp'
    with open(file_pass, mode='w') as f:
        f.write('// ' + json_dict[k]['description'] + '\n\n')
        for st in json_dict[k]['body']:
            f.write(st + '\n')

