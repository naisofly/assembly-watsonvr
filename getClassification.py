import requests
import json

images_file = open('images.txt','r')
images_json = open('classifiedImages.json', 'w')
default_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify'
version = '2016-05-20'
api_key = raw_input('[Visual Recognition] Enter the API key: ')
for line in images_file:
    line = line.rstrip()
    # classifier_ids = 'DOGE_1744879262,default'
    # url = default_url+'?&api_key='+api_key+'&url='+line+'&version='+version +'&classifier_ids='+classifier_ids
    url = default_url+'?&api_key='+api_key+'&url='+line+'&version='+version
    print url
    r = requests.get(url)
    data = json.dumps(r.json())
    print data
    #data = r.json()
    print >> images_json, data
