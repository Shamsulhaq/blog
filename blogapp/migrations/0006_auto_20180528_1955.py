# Generated by Django 2.0.5 on 2018-05-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20180528_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_at',
            field=models.DateField(auto_now=True),
        ),
    ]
