# First I need an app to deal with weibo api
# 这里开始模仿twitter爬虫开始制作
# pip3 install tweepy == 3.3

# 获取数据
# 利用OAuth验证
import tweepy
from tweepy import OAuthHandler

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Cursor逐条打印HOMEPAGE上的文字
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)


# create place-holder for personal implementation
def process_or_store(tweet):
    print(json.dumps(tweet))


# 或者改变命令，将其储存为json格式
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

# 如果我们需要所有我们的粉丝
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

# 如果需要将所有用户推特全部打印
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

# 如此这般，我们可以讲自己或者其他所有人（理论上）的所有推特内容保存为jason格式

# 数据的持续获取（串流）
# 我们需要调用streaming api
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

