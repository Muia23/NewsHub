from app import app
import urllib.request,json
from .models import news

Headline = news.Headline
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["HEADLINES_API_BASE_URL"]
category_url =app.config["NEWS_API_BASE_URL"]
def get_headlines(country):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = base_url.format(country,api_key)

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
        content = headline_item.get('content')
        url = headline_item.get('url')
        if author:
            headline_object = Headline(id,title,description,urlToImage,publishedAt,author,content,url)
            headline_results.append(headline_object)
    
    return headline_results

def get_headline(country):
    get_healine_details_url = base_url.format(country,api_key)

    with urllib.request.urlopen(get_headline_details_url) as url:
        headline_details_data = url.read()
        headline_details_response = json.loads(headline_details_data)

        headline_object = None
        if headline_details_response:
            id = headline_details_response.get('id')        
            title = headline_details_response.get('title')
            description = headline_details_response.get('description')
            urlToImage = headline_details_response.get('urlToImage')
            publishedAt = headline_details_response.get('publishedAt')
            author = headline_details_response.get('author')
            content = headline_details_response.get('content')
            content = headline_details_response.get('url') 

            headline_object = Headline(id,title,description,urlToImage,publishedAt,author,content,url)

    return headline_object

#category news
def get_category_news(category,country):
    '''
    Function that gets the json response to our url request
    '''
    get_category_news_url = category_url.format(category,country,api_key)

    with urllib.request.urlopen(get_category_news_url) as url:
        get_category_news_data = url.read()
        get_category_news_response = json.loads(get_category_news_data)

        category_news_results = None

        if get_category_news_response['sources']:
            category_new_results_list = get_category_news_response['sources']
            category_new_results = process_category_results(category_new_results_list)

    return category_new_results

def process_category_results(category_new_list):
    '''
    Function that process the category news result and transform them to a list of Objects

    Args:
        category_new_list: A list of dictionaries that containt headlines details

    Returns:
        category_new_results: A list of headline objects
    '''
    category_new_results = []
    for category_new_item in category_new_list:
        id = category_new_item.get('id')        
        name = category_new_item.get('name')
        description = category_new_item.get('description')
        url = category_new_item.get('url')
        if name:
            category_new_object = News(id,name,description,url)
            category_new_results.append(category_new_object)
    
    return category_new_results

def get_category_new(category,country):
    get_category_new_details_url = category_url.format(category,country,api_key)

    with urllib.request.urlopen(get_category_new_details_url) as url:
        category_new_details_data = url.read()
        category_new_details_response = json.loads(category_new_details_data)

        category_new_object = None
        if category_new_details_response:
            id = category_new_details_response.get('id')        
            name = category_new_details_response.get('name')
            description = category_new_details_response.get('description')            
            url = category_new_details_response.get('url') 

            category_new_object = News(id,name,description,url)

    return category_new_object