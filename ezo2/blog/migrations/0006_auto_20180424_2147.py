# Generated by Django 2.0.3 on 2018-04-24 19:47

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180406_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=markdownx.models.MarkdownxField(max_length=42),
        ),
    ]