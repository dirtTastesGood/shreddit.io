# Generated by Django 3.0.8 on 2020-08-02 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200802_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='profile_images/default.jpg', upload_to='profile_images/', verbose_name='profile image'),
        ),
    ]