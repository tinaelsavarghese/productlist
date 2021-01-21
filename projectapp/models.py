from django.db import models
class products(models.Model):

    edescription= models.CharField(max_length=100)
    ebaseunitofmeasure = models.CharField(max_length=100)
    eprojectunitofmeasure = models.CharField(max_length=100)
    econversionfactor = models.IntegerField()
    econtractingentryref = models.IntegerField()
    ematerialtype= models.CharField(max_length=100)
    emasterformatcode = models.IntegerField()
    euniformat = models.CharField(max_length=100)
    eRBScode= models.IntegerField()
    eWBSCODE=models.IntegerField()



# Create your models here.
