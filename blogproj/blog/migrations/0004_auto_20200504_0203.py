# Generated by Django 3.0.5 on 2020-05-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200504_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_good',
        ),
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
