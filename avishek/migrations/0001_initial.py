# Generated by Django 3.2.5 on 2021-07-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('details', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(default='placeholder.png', upload_to='thumbnails')),
                ('live_url', models.URLField(blank=True, null=True)),
                ('github_repo', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
