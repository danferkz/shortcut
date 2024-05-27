# Generated by Django 5.0.4 on 2024-05-27 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='cards',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('url_l', models.CharField(max_length=255)),
                ('url_s', models.CharField(max_length=255)),
                ('id_card', models.AutoField(primary_key=True, serialize=False)),
                ('tagName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'card',
                'verbose_name_plural': 'cards',
            },
        ),
    ]