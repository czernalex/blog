# Generated by Django 4.1.2 on 2022-10-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_thumb_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='full_img',
            field=models.ImageField(upload_to='full_imgs'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumb_img',
            field=models.ImageField(upload_to='thumb_imgs'),
        ),
    ]