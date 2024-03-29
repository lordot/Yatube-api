# Generated by Django 2.2.16 on 2022-11-01 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_remove_follow_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
