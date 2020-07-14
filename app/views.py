from flask import render_template
from app import app
from .request import get_headlines, get_station, get_category_news


# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting headline news
    source_headlines = get_headlines('us')   
    sports_category = get_category_news('sports','us')
    entertainment_category = get_category_news('entertainment','us')
    business_category = get_category_news('business','us')
    technology_category = get_category_news('technology','us')
    health_category = get_category_news('health','us')
    science_category = get_category_news('science','us')
    title = 'Home of Truthful and Unbiased News'
    return render_template('index.html', title = title, source = source_headlines, sports = sports_category, entertainment = entertainment_category, business = business_category, technology = technology_category, health = health_category, science = science_category)
    
@app.route('/news/<source>')
def news(source):
    '''
    view news page function that returns the headline details page and its data
    '''
    station = get_station(source)    

    return render_template('news.html',title = source , station = station)
    