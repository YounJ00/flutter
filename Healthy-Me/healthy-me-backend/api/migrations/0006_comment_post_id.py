# Generated by Django 3.1.5 on 2021-02-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210204_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.CharField(default='', max_length=5),
        ),
    ]