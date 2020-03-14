# Generated by Django 2.2.1 on 2020-02-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('hours_played', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]