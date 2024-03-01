from django.db import models
from django.contrib.auth.models import User
from career.models import career
from library.models import Module
    


class Stage(models.Model):
    Stage = models.IntegerField(verbose_name = "Etapa")
    application_date = models.DateField(
        verbose_name = "Fecha de aplicacion",
    )
    
   
    
    @property
    def year(self):
        return self.application_date.year
    
    
    @property
    def month(self):
        months = [ 'enero', 'febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        return months[self.application_date.month -1]
    
    def __str__(self):
        return f"{ self.Stage } - { self.month } { self.year}"
    
    class Meta:
        verbose_name = "Etapa"
        verbose_name = "Etapas"

# Create your models here.
class Exam(models.Model):
    user = models.OneToOneField(
        User, on_delete = models.CASCADE, 
        verbose_name = 'Usuarios')
    stage = models.ForeignKey(
        Stage, on_delete = models.CASCADE,
        verbose_name = 'Etapas')
    career = models.ForeignKey(
        career, on_delete = models.CASCADE,
        verbose_name = 'Carrera')
    modules = models.ManyToManyField(
        Module,
        through='ExamModule',
        verbose_name = 'Modulos'
    )
    score = models.FloatField( verbose_name = 'Calificacion',default = 0.0)
    
class ExamModule(models.Model):
    Exam = models.ForeignKey(
        Exam, on_delete = models.CASCADE,
        verbose_name = 'Examen')
    module = models.ForeignKey(
        Module, on_delete = models.CASCADE,
        verbose_name = 'Modulos')
    active = models.BooleanField(verbose_name = 'Activo', default = True)
    score = models.FloatField(verbose_name = 'Calificacion', default = 0.0)
    
