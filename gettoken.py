import urllib
import oauthlib
import config

request_token_url = 'hrrp://twitter.com/oauth/request_token'
access_token_url = 'http://twitter.com/oauth/access_token'
authenticate_url = 'http://twitter.com/oayth/authenticate'

CK = config.ConsumerKey
CS = config.ConsumerSecretKey

def getOauth():
    consumer = oauth.Consumer(CK,CS)
    client = oauth.Client(consumer)
    #request_tokenを取得
    resp, content = client.request(request_token_url, 'GET')
    request_token = dict(parse_qsl(content))