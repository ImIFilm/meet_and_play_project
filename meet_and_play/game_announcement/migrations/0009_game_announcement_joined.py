# Generated by Django 2.2 on 2019-04-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_announcement', '0008_auto_20190406_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_announcement',
            name='joined',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
