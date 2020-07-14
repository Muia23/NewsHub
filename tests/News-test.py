import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news_article = News(1,"It's just news","Nothing muchhhh...",'https://edition.cnn.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article,News))


