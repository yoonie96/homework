from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    rank = tr.select_one('td.number').text[0:2].strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text

    doc = {
        'rank':rank,
        'title':title,
        'artist':artist
    }

    db.genie.insert_one(doc)