from django.shortcuts import render
from .models import Post
from django.views import generic

# A python function or class, a middle man between the model and html code (template) AKA controller

class BlogView(generic.DetailView):
    model = Post
    template_name = "blog.html"