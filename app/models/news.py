class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,title,description,urlToImage,publishedAt,author):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author