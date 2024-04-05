# Generated by Django 5.0.4 on 2024-04-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('released', models.DateField()),
                ('runtime', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('writer', models.CharField(max_length=255)),
                ('actors', models.TextField()),
                ('plot', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('awards', models.TextField()),
                ('poster', models.URLField()),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
