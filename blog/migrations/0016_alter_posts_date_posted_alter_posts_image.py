# Generated by Django 4.0.3 on 2022-05-01 20:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_posts_date_posted_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 20, 17, 40, 667495, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='/profile_pics/default.jpg', upload_to='post_image'),
        ),
    ]
