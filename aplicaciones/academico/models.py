from tabnanny import verbose
from django.db import models
from django.utils.html import format_html
from .choices import sexos


class sede(models.Model):
    flial=models.CharField(max_length=20,verbose_name='filial')
    direccion=models.CharField(max_length=50, verbose_name='direccion')

    def nombre(self):
        return "{}, {}".format(self.flial,self.direccion)
    def __str__(self):
        return self.nombre()


class docente(models.Model):
    apellido_paterno=models.CharField(max_length=20,verbose_name='apellido paterno')
    apellido_materno=models.CharField(max_length=20,verbose_name='apellido materno')
    nombres=models.CharField(max_length=20,verbose_name='Nombre')
    fecha_nacimeinto=models.DateField(verbose_name='fecha de nacimeiento')
    sexo=models.CharField(max_length=1,choices=sexos,default='F') 

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno,self.apellido_materno,self.nombres)
    
    def __str__(self):
        return self.nombre_completo()
    
    class meta():
        verbose_name = 'docente'
        verbose_name_plural = 'docentes'
        db_table = 'docente'
        ordering = ['apellido_paterno','apellido_materno']
    
class curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente=models.ForeignKey(docente,null=True,blank=True,on_delete=models.CASCADE)
    sede=models.ForeignKey(sede,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        text="{0} ({1})"
        return text.format(self.nombre,self.creditos)
    def coloracion(self):
       if self.creditos>3:
            return format_html('<span style="color:green;">{0}</span>'.format(self.nombre))
       else:
            return format_html('<span style="color:red;">{0}</span>'.format(self.nombre))

class carrera(models.Model):
    nombre=models.CharField(max_length=20,verbose_name='nombre')
    duracion=models.PositiveSmallIntegerField()
    titulo=models.CharField(max_length=40,verbose_name='titulo')
    curso=models.ForeignKey(curso,blank=True,null=True,on_delete=models.CASCADE)

    def nombres(self):
        return "{} {} {}".format(self.nombre,self.duracion,self.titulo)
    def __str__(self):
        return self.nombres()



