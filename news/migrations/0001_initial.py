# Generated by Django 4.2.1 on 2023-06-06 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HackerNewsID',
            fields=[
                ('hackernews', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('fetched_at', models.DateTimeField(default=datetime.datetime(2023, 6, 6, 19, 12, 42, 133254))),
            ],
        ),
    ]