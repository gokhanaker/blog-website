# Generated by Django 2.0.13 on 2019-05-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190516_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(blank=True, upload_to='blog_post_images/'),
        ),
    ]
