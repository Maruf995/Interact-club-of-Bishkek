# Generated by Django 5.2.4 on 2025-07-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_alter_mailingpending_image_alter_volunteerform_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=3000)),
            ],
        ),
    ]
