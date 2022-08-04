from django.urls import path
from aplicaciones.academico.views import carreralistview, contacto, cursolistview,eliminar_curso,registrar_curso,edicion_curso,editar_curso,contacto

urlpatterns=[
    path('',cursolistview.as_view(), name='gestion_curso'),
    path('eliminarcurso/<int:id>', eliminar_curso),
    path('registrarcurso/',registrar_curso),
    path('edicioncurso/<int:id>',edicion_curso), #toma los datos del y redirige a la pagina
    path('editarcurso/',editar_curso), #editar los datos
    path('contacto/',contacto),
    path('carreras/',carreralistview.as_view())
]