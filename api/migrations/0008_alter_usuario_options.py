# Generated by Django 3.2.9 on 2021-11-22 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]