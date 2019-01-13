from newsapi import NewsApiClient

#setup
newsapi = NewsApiClient(api_key='0be597d2c65a4431b613c6ddf48777a1')

# The news api returns a json of 20 results per page
# we get the total results and divide by 20 to get the pages
# then adjust the queries to get all the pages
def getNews(searchParam):
  news = newsapi.get_everything(q=searchParam)
  
  totalResults = news['totalResults']
  numberOfPages = totalResults // 20

  articles = []

  # Now make request for every page
  for i in range(1, numberOfPages + 1):
    request = newsapi.get_everything(q=searchParam, page=i, language="en")

    # Append to articles
    if request['status'] == 'ok':
      for a in request['articles']:
        articles.append(a)

  finalJSON = {
    'status': news['status'],
    'totalResults': totalResults,
    'articles': articles
  }

  return finalJSON
