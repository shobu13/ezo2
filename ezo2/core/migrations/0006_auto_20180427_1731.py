# Generated by Django 2.0.3 on 2018-04-27 15:31

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_parametres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parametres',
            options={'verbose_name': 'Parametres', 'verbose_name_plural': 'Parametres'},
        ),
        migrations.RemoveField(
            model_name='parametres',
            name='a_propos_description',
        ),
        migrations.AddField(
            model_name='parametres',
            name='nom',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parametres',
            name='valeur',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]
