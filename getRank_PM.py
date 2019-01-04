# coding: UTF-8
from requests_html import HTMLSession
from datetime import datetime
import csv, time
import subprocess

time_flag = True

# 止まるんじゃねえぞ...
while True:
    # 現在時刻(秒)を取得
    while datetime.now().second != 59:
        #59分59秒ではないので1秒待つ
        time.sleep(1)
    
    # もう一秒待つ
    time.sleep(1)

    # 00分00秒になったぞ

    # csvファイルを追記モードで開く
    file = open('test.csv', 'a')
    writer = csv.writer(file, lineterminator = '\n')

    # csvに記述するやつを用意
    csv_list = []

    # 現在時刻を年月時分秒で取得
    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # リストの1カラム目に時間を記述
    csv_list.append(time_)

    #URLを文字列として宣言
    url = 'https://osu.ppy.sh/users/8341091'

    # URL先のページにアクセス
    session = HTMLSession()
    response = session.get(url)
    response.html.render()

    # div要素のclassがvalue-display__valueに設定されているものを取得
    # 複数classが設定されている可能性があるのでfirst=True
    element = response.html.find('div.value-display__value', first = True)

    # (要素).textで数値(要素タグで囲まれた文字列)を取得
    ranking = element.text
    
    # リストの2カラム目に時間を記述
    csv_list.append(ranking)
    # csvに追記敷く
    writer.writerow(csv_list)
    # 開けたら閉めようね
    file.close()

    # ターミナルにも出力(確認用)
    print (time_, ranking)

    subprocess.call('git commit -m "updateCSV" test.csv')
    subprocess.call('git push')
