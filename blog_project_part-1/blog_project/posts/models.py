from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta category ankgula post thakte pare 
#   abr ekta post er ankgula category thakte pare 
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        # cat_list = self.category.all()
        # category_name = []
        # for cat in cat_list:
        #     category_name.append(cat.name)
        # # categories = ', '.join(category_name)
        # # return f"{self.title} - {category_name}"
        return self.title