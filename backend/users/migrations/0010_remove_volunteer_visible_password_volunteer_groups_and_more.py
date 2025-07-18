# Generated by Django 5.1.6 on 2025-07-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0009_alter_volunteer_options_alter_volunteer_direction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='visible_password',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='login',
            field=models.CharField(max_length=100, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
