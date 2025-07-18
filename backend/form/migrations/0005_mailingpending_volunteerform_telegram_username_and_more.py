# Generated by Django 5.1.6 on 2025-07-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_alter_volunteerformarchive_moved_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingPending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Фамилия Имя')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('image', models.ImageField(blank=True, upload_to='media/users/', verbose_name='Фотография')),
                ('telegram_username', models.CharField(blank=True, max_length=100, verbose_name='Telegram юзернейм')),
            ],
        ),
        migrations.AddField(
            model_name='volunteerform',
            name='telegram_username',
            field=models.CharField(blank=True, max_length=100, verbose_name='Telegram @username'),
        ),
        migrations.AddField(
            model_name='volunteerformarchive',
            name='telegram_username',
            field=models.CharField(blank=True, max_length=100, verbose_name='Telegram @username'),
        ),
        migrations.AddField(
            model_name='waitinglist',
            name='telegram_username',
            field=models.CharField(blank=True, max_length=100, verbose_name='Telegram @username'),
        ),
    ]
