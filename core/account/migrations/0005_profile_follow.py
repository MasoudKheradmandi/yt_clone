# Generated by Django 4.1.3 on 2023-02-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_channel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(to='account.profile'),
        ),
    ]