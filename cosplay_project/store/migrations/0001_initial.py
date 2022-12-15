# Generated by Django 4.1.4 on 2022-12-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('image', models.URLField()),
                ('type', models.CharField(choices=[('weapon', 'Weapon'), ('clothe', 'clothe'), ('accessories', 'Accessories'), ('manga', 'Manga')], max_length=11)),
                ('publication_date', models.DateField(auto_now=True)),
            ],
        ),
    ]