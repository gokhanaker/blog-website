# Generated by Django 2.0.13 on 2019-05-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190516_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(default='media/default.png', upload_to='blog/media/blog_post_images/'),
        ),
    ]