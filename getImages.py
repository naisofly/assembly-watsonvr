import json
tweets_file = open('tweetdata.json', 'r')
images_file = open('images.txt','w')
for line in tweets_file:
    parsed_json = json.loads(line)
    if 'extended_entities' in parsed_json:
        tweet_text = parsed_json['text']
        tweet_picture = parsed_json['extended_entities']['media'][0]['media_url']
        # print tweet_text.encode('utf-8')
        # print tweet_picture
        images_file.write(tweet_picture)
        images_file.write('\n')
        print "==="
