# Generated by Django 4.2.2 on 2023-06-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_alter_moreinfo_genre_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Horror'), (3, 'Sci-Fi'), (4, 'Drama'), (2, 'Comedy'), (0, 'Another')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.PositiveSmallIntegerField(choices=[(0, '*'), (4, '*****'), (1, '**'), (3, '****'), (2, '***')], default=0),
        ),
    ]
