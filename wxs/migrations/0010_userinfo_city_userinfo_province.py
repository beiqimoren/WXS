# Generated by Django 4.2.11 on 2024-06-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxs', '0009_myconsultmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(default=11, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='province',
            field=models.CharField(default=22, max_length=32),
            preserve_default=False,
        ),
    ]
