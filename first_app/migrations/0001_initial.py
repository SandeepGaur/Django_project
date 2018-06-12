# Generated by Django 2.0.2 on 2018-06-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('technologies', models.CharField(max_length=150)),
                ('detail', models.TextField(max_length=500)),
                ('url_project', models.URLField()),
                ('github_link', models.CharField(max_length=150)),
            ],
        ),
    ]