from flask import render_template
from . import main

if __name__ == '__main__':
    
@main.app_errorhandler(404)
def error_404_page(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('error404.html'),404
    