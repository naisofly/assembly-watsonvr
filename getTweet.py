import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from watson_developer_cloud import ToneAnalyzerV3


#Use your keys
consumer_key = 'C0BtmLVmRVlvXi0rpyLD8Q6q2'
consumer_secret = 'XkoWKA2OE7HlKm6yFN6pqjDByTemANVhRQf9FQYY3SvPoP0MSi'
access_token = '2172304020-zlr4NnAzNUnQbiNo6Da1VTvKp29QzAJ18DEN9rX'
access_secret = 'Mh2pXut1DgcVVh8gsEM6IlBTqaFz0Buk9Ex8qkV7XJxlr'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# cprint & clean up the tweets to remove punctuations, hashtags, and other unwanted stuff #

end_strip = [".", ",", "?", "/", "!", "*", ":", ")", "'", '"']
start_strip = [":", "*", "(", "'", '"']

words = [] # a list to contain all the words in all the tweets

alltext = open('tweettext.txt', 'a')

tone_analyzer = ToneAnalyzerV3(
   username='aff6e203-0b37-4f5b-a8e5-fc62223b58d5',
   password='gK4joReK68Hv',
   version='2016-05-19 ')

class TweetListener(StreamListener):

    # def on_data(self, data):
    # #Open, write and close your file.
    #   with open('tweetdata.json','a') as tf:
	#   	  tf.write(data)
    #   return True

    def on_status(self, status):
      print "tweet " + str(status.created_at) +"\n"
      print status.text.encode('utf-8')  + "\n"
    #   print(json.dumps(tone_analyzer.tone(status.text.encode('utf-8')), indent=2))
      for word in status.text.split():
	  	  word = word.lower()
	  	  if word == "rt": # do not add to list if word is "rt"
	  	  	  break
	  	  for item in end_strip:
	  	  	  if word.endswith(item):
	  	  	  	  word = word[:-1]
	  	  for item in start_strip:
	  	  	  if word.startswith(item):
	  	  	  	  word = word[1:]
	  	  words.append(word)
	  	  alltext.write(word.encode('utf-8') + " ")


stream = Stream(auth, TweetListener(), secure=True, )
# t = u"IBM" # You can use different hashtags
# stream.filter(track=[t])
#stream.filter(follow="2172304020")
# stream.filter(track=['SWDXB16', 'IBMSWDXB16'])
stream.filter(track=['wendys','Baconator','Big Classic', 'Frosty Shake','burgers','fries','Cheeseburger','nugs', 'nuggets','#NuggsForCarter'], async=True)
# stream.filter(track=['@weratedogs', 'dogs', 'husky', 'huskies', 'dalmatian', 'dalmatians', 'beagle', 'beagles', 'Golden Retriever'], async=True)
