# Generated by Django 4.1.2 on 2022-10-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full_img',
            field=models.ImageField(blank=True, upload_to='full_imgs'),
        ),
    ]