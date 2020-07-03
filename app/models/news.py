class Headline:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,description,urlToImage,publishedAt,author):
        self.id =id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author