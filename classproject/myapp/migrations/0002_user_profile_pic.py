# Generated by Django 4.2.2 on 2023-06-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='None', upload_to='profile_pic/'),
            preserve_default=False,
        ),
    ]