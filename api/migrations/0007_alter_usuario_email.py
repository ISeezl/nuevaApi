# Generated by Django 3.2.9 on 2021-11-22 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_idusuario_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
