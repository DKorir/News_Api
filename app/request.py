from email.mime import image
import urllib.request,json
from .articles import ArticlesClas

from .sources import SourcesClass


#getting api key
api_key = None

# Getting the news base url
base_url = None    

def configure_request(app):
    global api_key_base_url
    api_key=app.config['NEWS_API_KEY']
    # base_url=app.config['API_BASE_URL']

def get_sources():
    get_sources_url='https://newsapi.org/v2/sources?apiKey=d2fd3e86d60440258ca5001e30e4854c'
    with urllib.request.urlopen(get_sources_url) as url:
        get_movies_data=url.read()
        get_movies_response = json.loads(get_movies_data)
    
        if get_movies_response['sources']:
            movie_results_list = get_movies_response['sources']
            movie_results = process_results(movie_results_list)
    return movie_results



def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        name = movie_item.get('name')
        time = movie_item.get('published_at')

        description = movie_item.get('description')
        url = movie_item.get('url')
        image = movie_item.get('image')
        author = movie_item.get('author')


        movie_object = SourcesClass(id,title,time,author,name,description,url,image)
        movie_results.append(movie_object)

    return movie_results



def get_articles(name):
    get_articles_url='https://newsapi.org/v2/top-headlines?sources={}&apiKey=d2fd3e86d60440258ca5001e30e4854c'.format(name)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response = json.loads(get_articles_data)
    
        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = results(article_results_list)
    return article_results





def results(article_list):

    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = ArticlesClass(id,name,author,title,description,urlToImage,url,publishedAt)
            article_results.append(article_object)

    return article_results

def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = cat_url.format(cat_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results



    

    