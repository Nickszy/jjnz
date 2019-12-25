from .models import Post
from django.shortcuts import render, get_object_or_404
import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


# Create your views here.

from django.http import HttpResponse

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions = ['markdown.extensions.extra',
                                        'markdown.extensions.codehilite', # 代码高亮
                                         'markdown.extensions.toc', # 目录
                                         TocExtension(slugify=slugify)])  
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})
