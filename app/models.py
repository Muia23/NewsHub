class Headline:
    '''
    Headlines class to define Headlines Objects
    '''

    def __init__(self,id,title,description,urlToImage,publishedAt,author,content,url):
        self.id =id    
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.author = author
        self.content = content
        self.url = url

class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url):
        self.id =id
        self.name =name
        self.description =description
        self.url = url