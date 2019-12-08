# coding: UTF-8
from requests_html import HTMLSession
from datetime import datetime
import csv
import time
import subprocess

# diffとるためのやつ
ranking_old = 75514
time_flag = True

# csvファイルを追記モードで開く
file = open('test.csv', 'a')
writer = csv.writer(file, lineterminator='\n')

# csvに記述するやつを用意
csv_list = []

# 現在時刻を年月時分秒で取得
time_ = datetime.now().strftime("%m%d")
# リストの1カラム目に時間を記述
csv_list.append(time_)

# URLを文字列として宣言
url = 'https://osu.ppy.sh/users/8341091'

# URL先のページにアクセス
session = HTMLSession()
response = session.get(url)
response.html.render()

# div要素のclassがvalue-display__valueに設定されているものを取得
# 複数classが設定されている可能性があるのでfirst=True
element = response.html.find('div.value-display__value', first=True)

# (要素).textでカンマ数値(要素タグで囲まれた文字列)を取得
ranking_raw = element.text
# カンマ数値(文字列)を数値に変換
ranking = int(ranking_raw.replace(',', ''))

# リストの2カラム目に時間を記述
csv_list.append(ranking)
# 3カラム目に前日比
csv_list.append(ranking_old - ranking)
ranking_old = ranking
# csvに追記敷く
writer.writerow(csv_list)
# 開けたら閉めようね
file.close()

# ターミナルにも出力(確認用)
print(time_, ranking)

'''
# 実行したいコマンド1(commit)
cmd_commit = "git commit -a -m update_CSV"
# Python上で外部コマンドを実行
subprocess.call(cmd_commit.split())
# 実行したいコマンド2(push)
cmd_push = "git push origin master"
subprocess.call(cmd_push.split())
'''