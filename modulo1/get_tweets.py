import json
import os
import time
import sys
from tweepy import OAuthHandler, Stream, StreamListener

class MyListener(StreamListener):

    def on_data(self, data):
        with open("tweets.txt", "a", encoding="UTF-8") as f:
            f.write(json.dumps(data) + "\n")

    def on_error(self, status):
        print(status)
    
    def on_exception(self, exception):
        print(exception)
        return

if __name__ == "__main__":
    api_key = os.environ.get("API_KEY")
    api_secret_key = os.environ.get("API_SECRET_KEY")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    listener = MyListener()
    auth = OAuthHandler(api_key, api_secret_key)  
    auth.set_access_token(access_token, access_token_secret)  
    stream = Stream(auth, listener)
    
    stream.filter(track=["Trump"], is_async=True)
    t = 60 if len(sys.argv) == 1 else int(sys.argv[1])
    time.sleep(t)
    stream.disconnect()