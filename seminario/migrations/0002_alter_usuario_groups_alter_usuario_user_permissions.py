# Generated by Django 5.1.6 on 2025-02-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('seminario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='seminario_usuario_set', related_query_name='usuario', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='seminario_usuario_set', related_query_name='usuario', to='auth.permission'),
        ),
    ]
