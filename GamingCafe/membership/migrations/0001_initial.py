# Generated by Django 2.2.1 on 2020-03-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('rank', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('eligibility', models.PositiveIntegerField()),
                ('discount_offered', models.PositiveIntegerField()),
            ],
        ),
    ]
