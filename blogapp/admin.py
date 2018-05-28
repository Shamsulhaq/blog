from django.contrib import admin
from . import models

# Register your models here.
class ArticleModel(admin.ModelAdmin):

    list_display = ['title', 'create_at']
    search_fields = ['details']
    list_filter = ['create_at']
    list_per_page = 10

    class Meta:
        Model = models.Article

admin.site.register(models.Article,ArticleModel)

admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Comments)

