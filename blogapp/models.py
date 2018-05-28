from django.db import models
from  django.contrib.auth.models import User




class Author (models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    profile_image = models.ImageField(upload_to = 'author', null=True)
    phone = models.CharField(max_length=15)
    details = models.TextField()

    def __str__(self):
        return self.name.username

class Category (models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article (models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to = 'article', null=True)
    create_at = models.DateField(auto_now_add=True,auto_now=False)
    update_at = models.DateField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.title
class Comments (models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.article.title
