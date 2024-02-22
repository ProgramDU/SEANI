from django.db import models
    


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
