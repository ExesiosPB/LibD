import flickrapi
import os
import requests

apiKey = '5c847904821a3d3a8fa77bd44bf59378'
apiSecret = 'fe691585e908cf7b'

flickr = flickrapi.FlickrAPI(apiKey, apiSecret, format='parsed-json')

def getAllPhotos(place):
  photosJSON = flickr.photos.search(tags=place)
  photos = photosJSON['photos']['photo']

  count = 0
  for photo in photos:
    fid = photo['farm']
    sid = photo['server']
    pid = photo['id']
    sec = photo['secret']

    # Flikr constructs static image url's like so
    # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
    url = 'https://farm{}.staticflickr.com/{}/{}_{}_m.jpg'.format(fid, sid, pid, sec)
    fname = '{}.jpg'.format(pid)
    # downloadImage(url, fname)

    # Now append photo url to main JSON
    photosJSON['photos']['photo'][count]['imageurl'] = url
    count += 1

  return photosJSON

def downloadImage(url, fname):
  if not os.path.isdir('./flikrimages/'):
    os.makedirs('./flikrimages/')

  fname = './flikrimages/{}'.format(fname)
  r = requests.get(url, stream=True)
  with open(fname, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
      f.write(chunk)
    return True
  return False

def getFlickr(search_param):
  return getAllPhotos(search_param)