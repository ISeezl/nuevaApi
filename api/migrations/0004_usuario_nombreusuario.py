# Generated by Django 3.2.9 on 2021-11-21 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nombreUsuario',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
