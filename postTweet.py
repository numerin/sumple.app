import json, config
from requests_oauthlib import OAuth1Session

CK = config.ConsumerKey
CS = config.ConsumerSecretKey
AT = config.AccessToken
AS = config.AccessSecretToken
twitter = OAuth1Session(CK, CS, AT, AS)

#ツイートポストエンドポイント
url = "https://api.twitter.com/1.1/statuses/update.json"

print("内容を入力してください")
tweet = input('>> ') #キーボード入力の取得
print('***************************************')

params = {"status" : tweet}

res = twitter.post(url, params = params) #post送信

if res.status_code == 200: #正常投稿できた場合
    print("Success.")
else:
    print("Failed. : %d" % res.status_code)