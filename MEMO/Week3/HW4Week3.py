import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    singerNames = song.select_one('td.info > a.artist.ellipsis')
    singer = singerNames.text.strip()
    songNames = song.select_one('td.info > a.title.ellipsis')
    ssong = songNames.text.strip()
    rankings = song.select_one('td.number')
    rank = rankings.text.split('\n')[0] #이게 어떤 원리로 나오는건지..?


    print(rank, ssong, singer)




