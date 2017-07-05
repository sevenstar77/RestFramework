from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_page(request):

    post_list = Post.objects.all()

    return HttpResponse('Hello : ' + post_list[0].title )