# Generated by Django 5.1.6 on 2025-07-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_volunteer_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteer',
            options={},
        ),
        migrations.AddField(
            model_name='volunteer',
            name='visible_password',
            field=models.CharField(blank=True, editable=False, max_length=100, verbose_name='Пароль (видимый)'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='password',
            field=models.CharField(blank=True, editable=False, max_length=100, verbose_name='Хеш пароля'),
        ),
    ]
