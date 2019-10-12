# Generated by Django 2.0.1 on 2018-06-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0012_userprofile_last_solve_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='author',
            field=models.CharField(default='Reznok', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_solve_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]