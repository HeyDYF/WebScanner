# Generated by Django 3.1.4 on 2021-01-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img_width',
            field=models.IntegerField(default=80, verbose_name='图片宽度'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.URLField(default='https://jwt1399.top/favicon.png', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=10, verbose_name='名称'),
        ),
    ]
