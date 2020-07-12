from flask import render_template
from app import app
from .request import get_headlines, get_headline, get_category_news, get_category_new


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
    title = 'Home of Truthful and Unbiased News'
    return render_template('index.html', title = title, source = source_headlines, sports = sports_category, entertainment = entertainment_category)    
    
@app.route('/news/<int:id>')
def news(id):
    '''
    view news page function that returns the headline details page and its data
    '''
    headline = get_headline(country)
    title = f'{headline.title}'

    return render_template('news.html',title = title, headline = headline)
    