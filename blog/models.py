from django.db import models
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)
    class Meta:
            verbose_name = '分类' 
            verbose_name_plural = verbose_name  #多个目录
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 70)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()

    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间', default=timezone.now)
    
    excerpt = models.CharField('摘要',max_length = 200,blank = True)

    category = models.ForeignKey(Category,verbose_name = '分类',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank = True)  #多对多的关系

    author = models.ForeignKey(User,verbose_name = '作者' , on_delete=models.CASCADE) #一对多


    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()  # 修改数据
        md = markdown.markdown(Exception = ['markdown.extensions.extra','markdown.extensions.codehilite'])
        self.excerpt= strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)        # 调用父类的save

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
