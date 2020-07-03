from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config['HEADLINES_API_BASE_URL']

def get_headlines(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = base_url.format(sources,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
            get_headlines_data = url.read()
            get_headlines_respone = json.loads(get_movies_data)

            headlines_results = None

            if get_headlines_respone['results']:
                headline_results_list = get_headlines_respone['results']
                headline_results = process_results(headline_results_list)

    return headline_results