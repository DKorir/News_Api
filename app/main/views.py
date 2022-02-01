from unittest import result
from flask import render_template,request,redirect,url_for

from . import main
from ..request import get_sources,get_articles,get_category


@main.route("/")
def index():
    popular_sources = get_sources() 
    bbc = get_articles('bbc-news') 
   
    return render_template('index.html',popular=popular_sources,results=bbc)

    

@main.route("/articles/<name>")
def articles(name):
    popular_sources = get_articles(name)
    
    return render_template('articles.html',results=popular_sources)

#categories
@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)
