# Generated by Django 2.0.13 on 2019-05-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190516_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(default='media/default.png', upload_to='media/blog_post_images/'),
        ),
    ]