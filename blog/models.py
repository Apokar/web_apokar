from django.db import models
import markdown
from django.utils.html import strip_tags
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name


class Post(models.Model):

    created_time = models.DateTimeField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    brief = models.CharField(max_length=100, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ForeignKey，即一对多的关联关系
    tags = models.ManyToManyField(Tag, blank=True)  # ManyToManyField，表明这是多对多的关联关系

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)