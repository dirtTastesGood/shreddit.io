# Generated by Django 3.0.8 on 2020-08-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200802_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='profile_images/default.jpg', upload_to='profile_images/', verbose_name='profile image'),
        ),
    ]