# Generated by Django 2.2 on 2019-05-07 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0005_auto_20190507_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_problems',
            name='date',
            field=models.CharField(default='NULL', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_problems',
            name='problem_type',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]