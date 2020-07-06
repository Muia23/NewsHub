from app import app
import urllib.request,json
from .models import news

Headline = news.Headline

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["HEADLINES_API_BASE_URL"]

def get_headlines(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = base_url.format(sources,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headline_results_list = get_headlines_response['articles']
            headline_results = process_results(headline_results_list)

    return headline_results

def process_results(headline_list):
    '''
    Function that process the headline result and transform them to a list of Objects

    Args:
        headline_list: A list of dictionaries that containt headlines details

    Returns:
        headline_results: A list of headline objects
    '''
    headline_results = []
    for headline_item in headline_list:
        id = headline_item.get('id')        
        title = headline_item.get('title')
        description = headline_item.get('description')
        urlToImage = headline_item.get('urlToImage')
        publishedAt = headline_item.get('publishedAt')
        author = headline_item.get('author')

        if author:
            headline_object = Headline(id,title,description,urlToImage,publishedAt,author)
            headline_results.append(headline_object)
    
    return headline_results