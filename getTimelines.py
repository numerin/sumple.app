import json, config
from requests_oauthlib import OAuth1Session

CK = config.ConsumerKey
CS = config.ConsumerSecretKey
AT = config.AccessToken
AS = config.AccessSecretToken
twitter = OAuth1Session(CK, CS, AT, AS)

#タイムライン取得エンドポイント
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params = {'count' : 5} #取得数
res = twitter.get(url, params = params)

if res.status_code == 200: #正常通信できた場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines:
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('***************************************')
else: #正常通信できなかった場合
     print("Failed: %d" % res.status_code)