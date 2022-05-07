# Generated by Django 4.0.3 on 2022-04-24 19:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_posts_date_posted_alter_posts_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='slug',
            new_name='heading',
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 24, 19, 39, 9, 272216, tzinfo=utc)),
        ),
    ]
