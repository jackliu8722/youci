# -*- coding=utf-8 -*-
'''
Created on 2012-7-14

@author: jackliu
'''
from datetime import datetime

weekdays = ["星期日",'星期一','星期二','星期三','星期四','星期五','星期六']
class BlogPost(object):
    """
    ths post information
    """
    def __init__(self,post = {}):
        self.postdict = post
    
    def day(self):
        datetime = self.postdict.get('posttime',None)
        if datetime:
            day = datetime.day
            if day < 10:
                return "0"+str(day)
            else:
                return str(day)
        else:
            return ""
    def month(self):
        datetime = self.postdict.get('posttime',None)
        if datetime:
            month = datetime.month
            if month < 10:
                return "0"+str(month)
            else:
                return str(month)
        else:
            return ""
    def year(self):
        datetime = self.postdict.get('posttime',None)
        if datetime:
            return datetime.year
        else:
            return ""
    def weekday(self):
        datetime = self.postdict.get('posttime',None)
        if datetime:
            global weekdays
            return weekdays[datetime.weekday()]
        else:
            return ""
    def time(self):
        datetime = self.postdict.get('posttime',None)
        if datetime:
            return datetime.strftime("%H:%M:%S")
        else:
            return ""
    def title(self):
        return self.postdict.get("title",'')
    def tags(self):
        return self.postdict.get('tags',[])
    def comments(self):
        return self.postdict.get('comments',[])
    def context(self):
        return self.postdict("context",'')
    




