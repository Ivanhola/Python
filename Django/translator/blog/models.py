from django.db import models
from django.contrib.auth.models import User

# A webpage has 3 components, Model, Views, Containers: Contains database fields of the page
# In Python MVC is referred to as MVT, where Model is the same, Views is templates (HTML code), and 
# Controller is the view in python.

STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    #Foreign key means the data will come from another table (User)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default = 0)

