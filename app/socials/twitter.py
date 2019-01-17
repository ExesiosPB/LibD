import tweepy
from tweepy.parsers import JSONParser

consumerKey = 'knQg8mg3KbnvgoGRXu44Ve4hs'
consumerSecretKey = 'BBVD4aW06v4fYpt539EeadxPGbpKFMwLCgQziCX91w5WwOiHax'
accessToken = '2583651299-5LZdduEwpUJzeCoapqn4cu4GCdBiDmh8EgWp3kk'
accessTokenSecret = 'zgjhiXtwnLUzP12K8OL5jxK1W8yEk75LzoI2uhAneFyF8'

# setup
auth = tweepy.OAuthHandler(consumerKey, consumerSecretKey)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, parser=JSONParser(), wait_on_rate_limit=True)

def getTweets(searchParam):
  displayCount = 100

  # Make initial request
  tweets = api.search(q=searchParam, count=displayCount)
  sinceId = tweets['statuses'][displayCount - 1]['id']

  # Now loop to get timeline of tweets
  statuses = []
  doneSearch = False
  count = 0;

  for s in tweets['statuses']:
    statuses.append({
      'created_at': s['created_at'],
      'favorite_count': s['favorite_count'],
      'retweet_count': s['retweet_count'],
      'text': s['text'],
      'user': {
        'followers_count': s['user']['followers_count'],
        'friends_count': s['user']['friends_count']
      }
    })

  while (doneSearch == False):
    # Make request and update sinceId, count
    tweets = api.search(q=searchParam, count=displayCount, since_id=sinceId)

    try:
      lastElem = tweets['statuses'][-1]
      sinceId = lastElem['id']
    except IndexError:
      doneSearch = True
    
    count += 1

    # Now create custom information to output back
    for s in tweets['statuses']:
      statuses.append({
        'created_at': s['created_at'],
        'favorite_count': s['favorite_count'],
        'retweet_count': s['retweet_count'],
        'text': s['text'],
        'user': {
          'followers_count': s['user']['followers_count'],
          'friends_count': s['user']['friends_count']
        }
      })

    # Checker to make sure we arent in infinite loop
    if (count > 500):
      doneSearch = True

  finalJSON = {
    'statuses': statuses
  }

  return finalJSON
  