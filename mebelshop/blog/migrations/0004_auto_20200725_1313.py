# Generated by Django 3.0 on 2020-07-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200723_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображения блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображения блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображения блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображения блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображения блога'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображения блога'),
        ),
    ]