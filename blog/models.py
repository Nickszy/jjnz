from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 100)
    class Meta:
            verbose_name = '分类'
            verbose_name_plural = verbose_name
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
    def save(self, *args, **kwargs):
            self.modified_time = timezone.now()
            super().save(*args, **kwargs)
    excerpt = models.CharField(max_length = 200,blank = True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank = True)  #多对多的关系

    author = models.ForeignKey(User,on_delete=models.CASCADE) #一对多

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
