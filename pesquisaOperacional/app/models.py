from django.db import models

# Create your models here.
class Variable(models.Model):
    
    numeroVariaveisDecisao = models.IntegerField(blank=True, null=False)
    numeroRestricoes       = models.IntegerField(blank=True, null=False)
    # method                 = models.BooleanField()
    
    
    '''def __str__(self):
        return self.numeroVariaveisDecisao'''