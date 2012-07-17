# coding:utf-8
from django.shortcuts import render_to_response
from youci import conf
from datetime import datetime
from youci.blogs import  model as blogmodel

def blog_index(request,template_name):
    title = "Jackliu的博客"
    testpost = {'posttime':datetime.now()}
    post = blogmodel.BlogPost(testpost)
    blogs = [post,post]
    menus = conf.blog_menu_language_zh
    links = conf.blog_friend_link_language_zh
    return render_to_response(template_name,locals())