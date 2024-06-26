# Generated by Django 4.2.11 on 2024-04-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxs', '0004_supporttable_alter_repairtable_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminID', models.IntegerField()),
                ('userID', models.IntegerField()),
                ('date', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=32)),
            ],
        ),
    ]
