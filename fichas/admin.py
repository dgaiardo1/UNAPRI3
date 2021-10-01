from django.contrib import admin

# Register your models here.
from fichas.models import Dependencia, Tarea, Ficha, OrigenDenuncia
from fichas.models import Delito, Estado, Juridiccione, Fiscale, DatosDefensoria
admin.site.register(Dependencia)
admin.site.register(OrigenDenuncia)
admin.site.register(Tarea)
admin.site.register(Ficha)
admin.site.register(Delito)
admin.site.register(Estado)
admin.site.register(Juridiccione)
admin.site.register(Fiscale)
admin.site.register(DatosDefensoria)


