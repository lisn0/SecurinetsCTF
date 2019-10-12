# Generated by Django 2.0.1 on 2018-05-23 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0007_remove_userprofile_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeSolve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf_framework.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='TitleGranted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf_framework.Title')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='completed_challenges',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='titles',
        ),
        migrations.AlterField(
            model_name='writeup',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf_framework.Challenge'),
        ),
        migrations.AlterField(
            model_name='writeup',
            name='markdown',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='writeup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf_framework.UserProfile'),
        ),
        migrations.AddField(
            model_name='titlegranted',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf_framework.UserProfile'),
        ),
        migrations.AddField(
            model_name='challengesolve',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf_framework.UserProfile'),
        ),
    ]
