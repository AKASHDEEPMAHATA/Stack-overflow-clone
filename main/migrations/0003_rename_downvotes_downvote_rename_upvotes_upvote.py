# Generated by Django 4.2.5 on 2023-09-20 17:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_upvotes_downvotes_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Downvotes',
            new_name='Downvote',
        ),
        migrations.RenameModel(
            old_name='Upvotes',
            new_name='Upvote',
        ),
    ]