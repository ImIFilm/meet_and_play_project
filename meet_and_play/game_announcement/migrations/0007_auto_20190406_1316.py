# Generated by Django 2.2 on 2019-04-06 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_announcement', '0006_auto_20190406_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_announcement',
            name='creator',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
