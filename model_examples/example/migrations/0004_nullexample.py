# Generated by Django 3.2.2 on 2021-05-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_dateexample'),
    ]

    operations = [
        migrations.CreateModel(
            name='NullExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]