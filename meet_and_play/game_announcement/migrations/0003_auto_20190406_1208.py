# Generated by Django 2.2 on 2019-04-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_announcement', '0002_auto_20190406_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_announcment',
            name='skill_level',
            field=models.CharField(choices=[('0', 'Recreational'), ('1', 'Amatuer'), ('2', 'Average'), ('3', 'Good'), ('4', 'Very Good')], max_length=100, verbose_name='Level of skills'),
        ),
        migrations.AlterField(
            model_name='game_announcment',
            name='sport',
            field=models.CharField(choices=[('0', 'Football'), ('1', 'Basketball'), ('2', 'Volleyball')], max_length=100, verbose_name='Sport'),
        ),
    ]