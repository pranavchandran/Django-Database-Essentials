# Generated by Django 3.2.2 on 2021-05-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_alter_framework_lanugage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Charachter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('movies', models.ManyToManyField(to='example.Movie')),
            ],
        ),
    ]