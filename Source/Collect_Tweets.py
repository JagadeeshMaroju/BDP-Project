import csv
import tweepy
from textblob import TextBlob
import dataset
from sqlalchemy.exc import ProgrammingError

db = dataset.connect("sqlite:///tweets.db")
csvFile = open('result_tweets.csv', 'a+')
csvWriter = csv.writer(csvFile)
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return
        print(status.text)
        blob = TextBlob(status.text)
        sent = blob.sentiment
        table = db["tweets"]
        try:
             table.insert(dict(
                user_description=str(status.user.description),
                user_location=str(status.user.location),
                coordinates=str(status.coordinates),
                text=str(status.text),
                user_name=str(status.user.screen_name),
                user_created=status.user.created_at,
                user_followers=str(status.user.followers_count),
                id_str=str(status.id_str),
                created=status.created_at,
                retweet_count=str(status.retweet_count),
                polarity=str(sent.polarity),
                subjectivity=str(sent.subjectivity),
            ))

        except ProgrammingError as e:
            print(e)

    def on_error(self, status_code):
        if status_code == 420:
            return False
twitter_key = 'gSEKhW3jUNeWSE7UDcx2FaGS5'
twitter_secret_key = 'bPlz8kEBJWsQqg6sVLuZaYcJO0b9WBBOFpxCJASwxk2TMdVO2E'
access_key = '1066068152-3qMacgRh4mYtA5WBA44ldHSyqO0qp25Vub4w9Ie'
access__secret_key = 'yYp4RGJDiQqh0XF2D6gBOopG3zaNcPlDpfmFAOZay3VMA'
authorization = tweepy.OAuthHandler(twitter_key, twitter_secret_key)
authorization.set_access_token(access_key, access__secret_key)
api = tweepy.API(authorization)
streamer = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamer)
stream.filter(track=["Democratic Party","Republican Party","Democrats","Republican","GOP","democratic","Republics"])