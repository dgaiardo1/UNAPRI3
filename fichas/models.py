from django.contrib import auth
from django.db import models


class Delito(models.Model):
    """Delitos."""
    delito = models.CharField(max_length=70,
                             help_text="Tipo de delito.")

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
                            help_text="Juridiccion Policial.")

    def __str__(self):
        return self.name


class Dependencia(models.Model):
    """Dependencia o Fiscalia."""
    name = models.CharField(max_length=50,
                            help_text="Dependencia.")
    email = models.EmailField(help_text="Mail de la Fiscalia o dependencia.")
    domicilio = models.CharField(max_length=50, blank=True,
                                 help_text="calle")

    def __str__(self):
        return self.name


class Fiscale(models.Model):
    """Fiscales"""
    apellido = models.CharField(max_length=50,
                            help_text="Apellido")
    nombre = models.CharField(max_length=50,
                            help_text="Nombre")
    direccion = models.CharField(max_length=50, help_text="Dirección")
    email = models.EmailField(help_text="Mail del Fiscal")
    telefono = models.CharField(max_length=50,
                            help_text="Telefono")
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

    def __str__(self):
        return self.name


class Tarea(models.Model):
    """Tareas del caso."""
    title = models.CharField(max_length=70,
                             help_text="Tarea.")
    dependencia = models.ForeignKey(Dependencia,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ficha(models.Model):
    """Ficha del caso"""
    caratula = models.CharField(max_length=50,null=True,
                                help_text="Carátula.")
    fechacierre = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="Fecha Creacion.")
    date_edited = models.DateTimeField(null=True,
                                       help_text="Ultima edicion.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE,
                             help_text="Dependencia.")

class DatosDefensoria(models.Model):
        """Datos de la Defensoria."""
        datos = models.CharField(max_length=70,
                                 help_text="Datos de la Defensoria.")
        ficha = models.ForeignKey(Ficha,
                                        on_delete=models.CASCADE)

        def __str__(self):
            return self.datos

