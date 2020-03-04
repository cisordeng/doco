import requests
import json
import lrc

def getKugou(word):
    names = []
    srcs = []
    lrcs = []
    imgs = []
    headers = {
        "Cookie": "kg_mid=645ab1323b9844ddf663fc2f6dd5ddc1;",
    }
    res = requests.get('https://songsearch.kugou.com/song_search_v2?&keyword='+word+'&clientver=&platform=WebFilter', headers=headers)
    jks = json.loads(res.text)
    jks = jks['data']['lists']
    hashs = []
    for jk in jks:
        hashs.append(jk['FileHash'])

    for hash in hashs:
        res = requests.get('https://www.kugou.com/yy/index.php?r=play/getdata&hash='+hash, headers=headers)
        jk = json.loads(res.text)
        jk = jk['data']
        names.append(jk['audio_name']+' -From Kugou')
        imgs.append(jk['img'])
        lrcs.append(jk['lyrics'])
        srcs.append(jk['play_url'])
    return names,srcs,lrcs

def getQQ(word):
    res1 = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w='+word)
    jm1 = json.loads(res1.text.strip('callback()[]'))
    jm1 = jm1['data']['song']['list']
    mids = []
    songmids = []
    srcs = []
    songnames = []
    singers = []
    names = []
    lrcs = []
    for j in jm1:
        try:
            mids.append(j['media_mid'])
            songmids.append(j['songmid'])
            #songnames.append(j['songname'])
            #singers.append(j['singer'][0]['name'])
            names.append(j['singer'][0]['name']+' - '+j['songname']+' -From QQmusic')
            lrcs.append(lrc.getLrc(j['singer'][0]['name']+' - '+j['songname']))
        except:
            print('wrong')

    for n in range(0,len(mids)):
        res2 = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+songmids[n]+'&filename=C400'+mids[n]+'.m4a&guid=6612300644')
        jm2 = json.loads(res2.text)
        vkey = jm2['data']['items'][0]['vkey']
        srcs.append('http://dl.stream.qqmusic.qq.com/C400'+mids[n]+'.m4a?vkey='+vkey+'&guid=6612300644&uin=0&fromtag=66')
    return names,srcs,lrcs

print(getKugou("远"))