import json
import requests
from bs4 import BeautifulSoup
def getLrc(word):
    try:
        url = 'http://so.1ting.com/lyric?q='+word
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        url = soup.select('.action_lrc')[0]['href']
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        result = soup.select('.center')[3].select('pre')[0].text
    except:
        result = '[00:00.00]You have a lrc file is empty~'
    return result
