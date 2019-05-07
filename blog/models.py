from django.db import models

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


    def __str__(self):
        return self.title

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
