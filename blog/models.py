from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    book_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    book_author = models.CharField(max_length=100)
    content = models.TextField()
    fave_quote = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)