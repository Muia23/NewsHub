import unittest
from models import news

Headline = news.Headline

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Headline('Python is craxy','Boring python series','https://www.emerce.nl/content/uploads/2020/06/shutterstock_720579289.jpg',"2020-07-03T10:00:23Z","Muia")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Headline))

if __name__ == '__main__':
    unittest.main()

