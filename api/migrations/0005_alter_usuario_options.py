# Generated by Django 3.2.9 on 2021-11-22 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_usuario_nombreusuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['nombreUsuario'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
