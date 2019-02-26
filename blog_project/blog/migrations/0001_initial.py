# Generated by Django 2.0.13 on 2019-02-26 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentContent', models.TextField()),
                ('commentCreatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('commentLikes', models.IntegerField(default=0)),
                ('commentDislikes', models.IntegerField(default=0)),
                ('commentAuthor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('postContent', models.TextField()),
                ('postCreatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('postLikes', models.IntegerField(default=0)),
                ('postAuthor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
