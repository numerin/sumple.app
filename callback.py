from requests_oauthlib import OAuth1Session
from urllib.parse import parse_qsl
import config

CK = config.ConsumerKey
CS = config.ConsumerSecretKey
AT = config.AccessToken
AS = config.AccessSecretToken
twitter = OAuth1Session(CK, CS, AT, AS)
request_token_url = ''

oauth_callback = "https://127.0.0.1:5000/oauth/twitter/callback"

response = twitter.post(
    request_token_url,
    params={'oauth_callback': oauth_callback}
)

#responseからリクエストトークンを取り出す
request_token = dict(parse_qsl(response.content.decode("utf-8")))

#リクエストトークンから連携画面のURLを作成
authenticate_url = "http://api.twitter.com/oauth/authenticate"
authenticate_endpoint = '%s?oauth_token=%s'\
    %(authenticate_url, request_token['oauth_token'])

print(authenticate_endpoint)