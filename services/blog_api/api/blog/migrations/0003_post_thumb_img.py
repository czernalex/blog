# Generated by Django 4.1.2 on 2022-10-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_full_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb_img',
            field=models.ImageField(blank=True, upload_to='thumb_imgs'),
        ),
    ]