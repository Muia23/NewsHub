from flask import render_template
from app import app
from .request import get_headlines


# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting headline news
    cnn_headlines = get_headlines('cnn')
    print(cnn_headlines)
    title = 'Home of Truthful and Unbiased News'
    return render_template('index.html', title = title, cnn = cnn_headlines)

@app.route('/news/<news_id>')
def news(news_id):
    '''
    view news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
    