from django.contrib import admin
from .models import carrera, curso,docente,sede

#admin.site.register(curso)
@admin.register(curso)
class cursoadmin(admin.ModelAdmin):
    list_display=('id','coloracion','creditos')
    #list_editable=('nombre','creditos')
    #list_display_links=('nombre',)
    #list_per_page: 2
  
  
    """
    fieldsets =(
        (None,{
            'fields':('nombre',)
        }),
        ('Advanced options',{
            'classes':('collapse','wide','extrapretty'),
            'fields':('creditos',)
        })
    )
   """
    def datos(self,obj):
        return obj.nombre.upper()
    
    datos.short_description="MATERIAs"
    datos.admin_order_field='id'

#admin.site.register(curso,cursoadmin)
admin.site.register(docente)
admin.site.register(sede)

@admin.register(carrera)
class carreras(admin.ModelAdmin):
    list_display=('id','nombre','duracion','titulo','curso')

