from django.contrib import auth
from django.db import models


class Delito(models.Model):
    """Delitos."""
    delito = models.CharField(max_length=70, help_text="Tipo de delito.")

    def __str__(self):
        return self.delito


class Estado(models.Model):
    """Dependencia o Fiscalia."""
    name = models.CharField(max_length=50,
                            help_text="Estado de Situacion.")

    def __str__(self):
        return self.name


class Juridiccione(models.Model):
    """Juridiccion Policial."""
    name = models.CharField(max_length=50,
                            help_text="Juridiccion")

    def __str__(self):
        return self.name


class Localidade(models.Model):
    """Localidad."""
    name = models.CharField(max_length=50,
                            help_text="Localidad.")
    idjuridiccion = models.ForeignKey(Juridiccione, on_delete=models.CASCADE)
    CP = models.CharField(max_length=6,
                          help_text="Codigo postal", blank=True)

    def __str__(self):
        return self.name


class RolAdministrativo(models.Model):
    """Rol Administrativo dentro de la Dependencia."""
    rolAdministrativo = models.CharField(max_length=50, help_text="Rol Administrativo.")

    def __str__(self):
        return self.rolAdministrativo


class JuridiccionesPoliciale(models.Model):
    """Juridiccion Policial."""
    name = models.CharField(max_length=50,
                            help_text="Juridiccion Policial.")
    idlocalidad = models.ForeignKey(Localidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dependencia(models.Model):
    """Dependencia o Fiscalia."""
    name = models.CharField(max_length=50,
                            help_text="Dependencia.")
    idLocalidad = models.ForeignKey(Localidade, on_delete=models.CASCADE)
    email = models.EmailField(help_text="Mail de la Fiscalia o dependencia.")
    domicilio = models.CharField(max_length=50, blank=True,
                                 help_text="domicilio")

    def __str__(self):
        return self.name


class Administrativo(models.Model):
    """Usuarios."""
    usuario = models.CharField(max_length=70,
                               help_text="usuario.", unique=True)
    apellido = models.CharField(max_length=70,
                                help_text="apellido.")
    nombre = models.CharField(max_length=70,
                              help_text="nombre.")
    telefono = models.CharField(max_length=70,
                                help_text="telefono.")
    mail = models.EmailField(max_length=30,
                             help_text="mail.")
    iddependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario


class Fiscale(models.Model):
    """Fiscales"""
    apellido = models.CharField(max_length=50, help_text="Apellido")
    nombre = models.CharField(max_length=50, help_text="Nombre")
    direccion = models.CharField(max_length=50, help_text="Dirección")
    email = models.EmailField(help_text="Mail del Fiscal")
    telefono = models.CharField(max_length=50, help_text="Telefono")
    dependencia = models.ForeignKey(Dependencia,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class OrigenDenuncia(models.Model):
    """Origen de la denuncia."""
    name = models.CharField(max_length=50,
                            help_text="Origen de la Denuncia.")
    direccion = models.CharField(max_length=50, help_text="Direción")
    email = models.EmailField(help_text="Mail.")
    telefono = models.CharField(max_length=15, blank=True, help_text="Telefono")

    def __str__(self):
        return self.name


class Ficha(models.Model):
    """Ficha del caso"""
    caratula = models.CharField(max_length=50, null=True,
                                help_text="Carátula.")
    pex = models.CharField(max_length=50, help_text="PEX")
    fechacierre = models.DateField(null=True)
    fechacreacion = models.DateTimeField(auto_now_add=True, help_text="Fecha Creacion.")
    violenciadegenero = models.BooleanField(help_text="Violencia de Genero")
    ultimaedicion = models.DateTimeField(null=True, help_text="Ultima edicion.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE, help_text="Dependencia.")
    fechahecho = models.DateField(null=True)
    etapa = models.CharField(max_length=30, help_text="Etapa del Caso")
    imputado = models.BooleanField(help_text="Tiene imputados")
    detenidos = models.BooleanField(help_text="Detenidos")
    flagrancia = models.BooleanField(help_text="Flagrancia")
    autoresIgnorados = models.BooleanField(help_text="Autores Ignorados")
    victimaDesconocida = models.BooleanField(help_text="Victima Desconocida")
    idViaDenuncia = models.ForeignKey(OrigenDenuncia, on_delete=models.CASCADE)
    idFiscalAdjunto = models.CharField(max_length=50, help_text="Fiscal Adjunto")
    idJuridiccionPolicial = models.ForeignKey(JuridiccionesPoliciale, on_delete=models.CASCADE)
    idFiscalaCargo = models.ForeignKey(Fiscale, on_delete=models.CASCADE)
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    resumendelaDenuncia = models.Field(max_length=300, blank=True, help_text="Resumen de la denuncia")


class Tarea(models.Model):
    """Tareas del caso."""
    ESTADOS = (
        ('I', 'Iniciado'),
        ('T', 'Terminado'),
        ('C', 'Cancelado'),
    )
    estados = models.CharField(max_length=1, choices=ESTADOS)
    descripcionTarea = models.CharField(max_length=70,
                                        help_text="Tarea.")
    fechaSolicitud = models.DateField()
    notaContextual = models.CharField(max_length=300, help_text="Nota contextual")
    fechaConclusion = models.DateField(help_text="Fecha de Conclusion de la tarea")
    idAdministrativo = models.ForeignKey(Administrativo, on_delete=models.CASCADE)
    nota = models.CharField(max_length=300, null=True, help_text="Nota")
    resultado = models.FileField(help_text="resultado", null=True)
    idDependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    idCaso = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcionTarea


class Ubicacione(models.Model):
    """Ubicaciones (Ej: Mesa de entrada, Secretario, Delitos Complejos)."""
    ubicacion = models.CharField(max_length=50,
                                 help_text="Dependencia.")
    idDependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    idCaso = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.ubicacion


class DatosDefensoria(models.Model):
    """Datos de la Defensoria."""
    datos = models.CharField(max_length=70, help_text="Datos de la Defensoria.")
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.datos


class Foto(models.Model):
    """Fotos."""
    name = models.CharField(max_length=50,
                            help_text="Descripcion de la Imagen.")
    archivoFoto = models.FileField(help_text="Foto.")
    idCaso = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(models.Model):
    """Video."""
    name = models.CharField(max_length=50,
                            help_text="Descripcion del video.")
    archivoVideo = models.FileField(help_text="Video.")
    idCaso = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Archivo(models.Model):
    """Video."""
    name = models.CharField(max_length=50,
                            help_text="Descripcion del Archivo.")
    archivoVideo = models.FileField(help_text="Video.")
    idCaso = models.ForeignKey(Ficha, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
