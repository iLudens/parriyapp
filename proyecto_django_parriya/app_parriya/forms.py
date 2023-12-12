from django import forms
from .models import Usuario, Recetas, Parrilleros, Disponibilidad, Reserva


STATUS_CHOICES = [
    (0, 'Inactivo'),
    (1, 'Activo'),
]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellidos',
            'contrasena',
            'email',
            'edad',
            'peso',
            'altura',
            'fecha_nacimiento',
            'roles',
        ]


class RecetaForm(forms.ModelForm):
    re_image = forms.ImageField()

    class Meta:
        model = Recetas
        fields = [
            're_title',
            're_desc',
            're_image',
            're_total_group',
            're_minutes',
            're_difficulty',
            're_status'
        ]

        DIFFICULTY_CHOICES = [
            (0, 'Muy Fácil'),
            (1, 'Fácil'),
            (2, 'Intermedio'),
            (3, 'Dífil'),
            (4, 'Muy Díficil'),
        ]

        labels = {
            're_title': 'Título',
            're_desc': 'Descripción',
            're_image': 'Imagen',
            're_total_group': 'Total Personas',
            're_minutes': 'Minutos',
            're_difficulty': 'Dificultad',
            're_status': 'Estado',
        }

        widgets = {
            're_title': forms.TextInput(attrs={'class': 'form-control'}),
            're_desc': forms.TextInput(attrs={'class': 'form-control'}),
            're_total_group': forms.TextInput(attrs={'class': 'form-control'}),
            're_minutes': forms.TextInput(attrs={'class': 'form-control'}),
            're_difficulty': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-select'}),
            're_status': forms.Select(choices=DIFFICULTY_CHOICES, attrs={'class': 'form-select'}),
        }


class ParrillerroForm(forms.ModelForm):
    class Meta:
        model = Parrilleros
        fields = [
            'pa_name',
            'pa_desc',
            'pa_profile',
            'pa_status',
        ]


class DispoForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = '__all__'
    fechaDispo = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label= 'Fecha Disponible')

class ResForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = 'nSolicitante', 'infoReserva'
        
        labels = {
                'nSolicitante': 'Nombre Solicitante',
                'infoReserva': 'Datos para Reservar'

            }
    

    nSolicitante = forms.TextInput()
    
    infoReserva = forms.ChoiceField(choices=[], required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disponibilidad = Disponibilidad.objects.filter(estado='disponible')
        choices = [(f"{dispos.idDispo}", f"{dispos.nombre} - {dispos.fechaDispo} - {dispos.horario}") for dispos in disponibilidad]
        self.fields['infoReserva'].choices = choices

    def save(self, commit=True):
        reserva = super().save(commit=False)
        idDispo = self.cleaned_data['infoReserva']
        disponibilidad = Disponibilidad.objects.get(idDispo=idDispo)
        
        # Guardar los campos deseados de Disponibilidad en infoReserva de Reserva
        reserva.infoReserva = f"{disponibilidad.nombre} - {disponibilidad.fechaDispo} - {disponibilidad.horario}"

        if commit:
            reserva.save()
            
            # Actualizar el estado de la disponibilidad
            disponibilidad.estado = 'ocupado'
            disponibilidad.save()

        return reserva
