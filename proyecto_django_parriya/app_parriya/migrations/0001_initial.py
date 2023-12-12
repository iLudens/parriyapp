# Generated by Django 4.2.7 on 2023-11-21 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=30, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('edad', models.PositiveIntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.FloatField()),
                ('fecha_nacimiento', models.DateField()),
                ('ultimo_login', models.DateTimeField(auto_now=True)),
                ('esta_activa', models.BooleanField(default=True)),
                ('es_personal', models.BooleanField(default=False)),
                ('roles', models.CharField(choices=[('usuario', 'Usuario normal'), ('parrillero', 'Parrillero'), ('admin', 'Administrador')], default='usuario', max_length=10)),
            ],
        ),
    ]
