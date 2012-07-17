# coding:utf-8
from django.shortcuts import render_to_response

from youci import conf

def homepage(request):
    title = '欢迎来到Jackliu的个人主页'
    menus = conf.blog_menu_language_zh
    links = conf.blog_friend_link_language_zh
    return render_to_response('index.html',locals())

def test(request):
    title = 'test'
    menus = conf.blog_menu_language_zh
    links = conf.blog_friend_link_language_zh
    return render_to_response('test.html',locals())


