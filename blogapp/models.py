from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Author (models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    profile_image = models.FileField(blank=True)
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
    image = models.FileField()
    create_at = models.DateField(auto_now_add=True,auto_now=False)
    update_at = models.DateField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.title
