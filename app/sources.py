class SourcesClass:

    def __init__(self,id,title,time,author,name,description,url,image):
        self.id=id
        self.title=title
        self.name=name
        self.description=description
        self.time=time
        self.author=author
        self.image=image
        self.url=url
        
        

class Category:
    '''
    Class that instantiates objects of the news categories objects of the news sources
    '''
    def __init__(self,id,name,author,description,time,url,image,title):
        self.id = id
        self.author = author
        self.name=name
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title


