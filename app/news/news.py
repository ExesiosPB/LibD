from newsapi import NewsApiClient

#setup
newsapi = NewsApiClient(api_key='0be597d2c65a4431b613c6ddf48777a1')

def getNews():
  news = newsapi.get_everything(q='Stoke-on-Trent', language="en")
  return news
  