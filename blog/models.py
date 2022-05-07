from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .helpers import *
from froala_editor.fields import FroalaField

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics',default='default.jpeg')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        self.slug =generate_slug(self.title)
        super(Posts, self).save(*args,**kwargs)
