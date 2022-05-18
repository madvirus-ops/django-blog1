from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .helpers import *
from PIL import Image
import os
from uuid import uuid4

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'post_image'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    slug = models.SlugField(max_length=1000,null=True, blank=True)
    image = models.ImageField(upload_to=path_and_rename, max_length=100, null=True, blank=True, default='default.jpeg')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        self.slug =generate_slug(self.title)
        super(Posts, self).save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)






