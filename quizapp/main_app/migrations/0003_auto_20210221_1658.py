# Generated by Django 3.1.6 on 2021-02-21 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_quiz_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='Level',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='correctAnswer',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='hint',
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='category',
            field=models.CharField(default='JRJS & US', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='difficulty',
            field=models.CharField(default='easy', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='incorrect_answers',
            field=models.CharField(default=1, max_length=700),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
