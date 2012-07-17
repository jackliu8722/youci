from django.db import models

# Create your models here.

class ArticleType(models.Model):
    type_name = models.CharField(max_length = 30)

class Tags(models.Model):
    tag_name = models.CharField(max_length = 20) 

class Article(models.Model):
    subject = models.CharField(max_length = 60)
    type = models.ForeignKey(ArticleType)
    publication_time = models.DateTimeField()
    last_modification_time = models.DateTimeField()
    content = models.TextField()
    tags = models.ManyToManyField(Tags)
    view_count = models.IntegerField()
class Comment(models.Model):
    article = models.ForeignKey(Article) 
    content = models.CharField(max_length = 200)
    ip_address = models.IPAddressField()
    area = models.CharField(max_length = 20)
    comment_time = models.DateTimeField()
    article = models.ForeignKey(Article)    