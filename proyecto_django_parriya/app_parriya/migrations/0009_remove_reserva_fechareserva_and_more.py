# Generated by Django 4.2.5 on 2023-12-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_parriya', '0008_reserva_disponibilidad_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fechaReserva',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='nParrillero',
        ),
        migrations.AddField(
            model_name='reserva',
            name='infoReserva',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]