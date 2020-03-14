# Generated by Django 2.2.1 on 2020-03-01 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membership', '0003_auto_20200301_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_left', models.PositiveIntegerField(default=0)),
                ('total_time', models.PositiveIntegerField(default=0)),
                ('join_date', models.DateTimeField()),
                ('membership_status', models.ForeignKey(default='The Warrior', on_delete=django.db.models.deletion.CASCADE, to='membership.Membership')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
