import unittest
from app.models import Headline

class HeadlineTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headline = Headline(1,"End times","Are upon us!!!!!!",'https://www.emerce.nl/content/uploads/2020/06/shutterstock_720579289.jpg',"2020-07-03T10:00:23Z","Muia","I'm not sure though",'https://edition.cnn.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,Headline))


