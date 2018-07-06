import tweepy 
import json

API_KEY="Bo1vf2L1OmveFqiBYm795oZw5"
API_SECRET="8IqLq6r1VNRuVt9C4heLj4hQuxHDo5suG6L37cyMhUFHhJCw2g"
ACCESS_TOKEN="1456538761-mVv2N1ZnVx5lW7P9UzDUTP660Kd36Z9aUT0RqgN"
ACCESS_TOKEN_SECRET="lfLoGrucOSP6YU8ImrzQ99UZd7kbGuPNIEppChvfKhibb"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

api.update_profile_image('twitterdog.jpg')
