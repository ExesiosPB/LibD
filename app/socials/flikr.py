import flickrapi
import json
import sys

apiKey = '5c847904821a3d3a8fa77bd44bf59378'
apiSecret = 'fe691585e908cf7b'

def getFlickr():
  flickr = flickrapi.FlickrAPI(apiKey, apiSecret, format='json')
  rawJSON = flickr.photos.search(tags='stoke')
  parsed = json.loads(rawJSON.decode('utf-8'))
  
  print(parsed, file=sys.stderr)