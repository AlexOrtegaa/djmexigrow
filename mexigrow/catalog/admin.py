from django.contrib import admin
from .models import Proyect
from .models import ProyectInstance

# Register your models here.


@admin.register(Proyect)

class ProyectAdmin(admin.ModelAdmin):
    list_filter = ('title', 'company', 'date_published')
    list_display = ('id', 'title', 'company', 'date_published')
@admin.register(ProyectInstance)
class ProyectInstanceAdmin(admin.ModelAdmin):
    list_filter = ('id','proyect', 'date_acquired', 'date_of_end_contract', 'investment', 'investor')
    list_display = ('id', 'proyect', 'date_acquired', 'date_of_end_contract', 'investment', 'investor')

