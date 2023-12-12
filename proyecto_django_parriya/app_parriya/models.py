from django.db import models


def content_image_upload_to(instance, filename):
    base_path = f'static/wwwroot/sur/images/content_images/{instance.unique_id}'
    return os.path.join(base_path, f"{instance.re_title}.png")


class Usuario(models.Model):
    # Campos de texto
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    # Campos numéricos
    edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()

    # Campos de fechas
    fecha_nacimiento = models.DateField()
    ultimo_login = models.DateTimeField(auto_now=True)

    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('parrillero', 'Parrillero'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(
        max_length=10, choices=OPCIONES_ROL, default='usuario')


DIFFICULTY_CHOICES = [
    (0, 'Muy Fácil'),
    (1, 'Fácil'),
    (2, 'Intermedio'),
    (3, 'Dífil'),
    (4, 'Muy Díficil'),
]

STATUS_CHOICES = [
    (0, 'Inactivo'),
    (1, 'Activo'),
]


class Recetas(models.Model):
    id = models.AutoField(primary_key=True)
    re_title = models.CharField(max_length=255, null=False, blank=False)
    re_desc = models.TextField()
    re_image = models.ImageField(upload_to='static/img/', null=True)
    re_total_group = models.IntegerField()
    re_minutes = models.IntegerField()
    re_difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=0)
    re_slug = models.CharField(max_length=512)
    re_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Parrilleros(models.Model):
    id = models.AutoField(primary_key=True)
    pa_name = models.CharField(max_length=255, null=False, blank=False)
    pa_desc = models.TextField()
    pa_profile = models.ImageField(
        upload_to='static/img/parrillero/profile', null=True)
    pa_slug = models.CharField(max_length=512)
    pa_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


OPCIONES_JORNADA = [
    ('manana', '09:00 - 13:59'),
    ('tarde', '14:00 - 18:59'),
    ('noche', '19:00 - 01:59'),
]
horario = models.CharField(max_length=30, choices=OPCIONES_JORNADA)

OPCIONES_ESTADODISPO = [
    ('disponible', 'DISPONIBLE'),
    ('ocupado', 'OCUPADO'),
]


class Disponibilidad(models.Model):
    idDispo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fechaDispo = models.DateField()
    horario = models.CharField(max_length=30, choices=OPCIONES_JORNADA)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADODISPO)

    def __str__(self):
        return "{}". format(self.nombre)


class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    nSolicitante = models.CharField(max_length=50)
    infoReserva = models.CharField(max_length=200)


