from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def path_and_rename(instance, filename):
    upload_to = 'profile_pics'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Profile(models.Model):
    verified = models.BooleanField(default=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to=path_and_rename)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
