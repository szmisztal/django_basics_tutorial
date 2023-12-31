# Generated by Django 4.2.2 on 2023-06-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0006_alter_moreinfo_genre_alter_rating_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='genre',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Comedy'), (3, 'Sci-Fi'), (4, 'Drama'), (1, 'Horror'), (0, 'Another')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='time',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, '*****'), (0, '*'), (2, '***'), (1, '**'), (3, '****')], default=0, null=True),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('movies', models.ManyToManyField(related_name='actor', to='filmyweb.movie')),
            ],
        ),
    ]
