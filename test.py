# coding: UTF-8
import urllib3
from bs4 import BeautifulSoup
import json
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
import urllib.request
import os

# アクセスするURL
header = "https://www.keio.co.jp/unkou/"
link = "unkou_pc.html"
url = header + link

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
http = urllib3.PoolManager()
r = http.request('GET', url)
soup = BeautifulSoup(r.data, 'html.parser')

# タイトル要素を取得する
status_tag = soup.find(class_="status")

status = status_tag.get_text().strip()
print(status)

# 路線図の取得(もっときれいに書けるはず)
if "京王線・井の頭線は平常通り運転しています。" != status:
	for image in soup.findAll("img"):
		# if image.get("alt") == "運行情報":
		if image.get("alt") == "路線図":
			# print(header + image.get('src'))
			png_link_cmd = "curl -o /tmp/unkou.tmp.png " + header + image.get('src') + "> /dev/null 2>&1"
			os.system(png_link_cmd)
			os.system("imgcat /tmp/unkou.tmp.png")

# 要素の文字列を取得する
#他社線から振替輸送による混雑の為、京王線は一部列車に運休と、上下線に１５分程度の遅れが出ています。振替輸送をご利用下さい。なお、京王ライナー１〜１１号は本日運休いたします。ＪＲ山手線：新宿〜渋谷間ＪＲ中央線：新宿〜高尾間ＪＲ南武線：武蔵小杉〜立川間ＪＲ武蔵野線：府中本町〜西国分寺間ＪＲ横浜線：長津田〜八王子間多摩モノレール：立川北・南〜多摩センター間東京メトロ　丸ノ内線：赤坂見附〜荻窪・方南町間東京メトロ　銀座線：赤坂見附〜渋谷間東京メトロ　副都心線：渋谷〜新宿三丁目間東京メトロ　千代田線：表参道〜代々木上原間都営地下鉄　新宿線：全線都営地下鉄　大江戸線：全線都営地下鉄　三田線：全線都営地下鉄　浅草線：全線小田急線：新宿〜町田・唐木田間東急　世田谷線：下高井戸〜三軒茶屋間東急　田園都市線：渋谷〜長津田間東急　東横線：渋谷〜武蔵小杉間東急　大井町線：自由が丘〜溝の口間西武　多摩川線：是政〜武蔵境間

#京王線・井の頭線は平常通り運転しています。

# 鉄道.comのRSSのまとめ(JSON)の解析
'''
url = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'
res = urllib.request.urlopen(url)
# res = urllib3.urlopen("https://rti-giken.jp/fhc/api/train_tetsudo/delay.json")
datas = json.loads(res.read())
for d in datas:
	print(d['name'])
'''


