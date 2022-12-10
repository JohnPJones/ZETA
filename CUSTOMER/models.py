from django.db import models

# Create your models here.
Lotus_Salary_Base_Choices = (
    ('SOUTH_PATTAYA','SOUTH PATTAYA'),
    ('U-TAPAO','U-TAPAO')
)

class CustomerInputModel(models.Model):
    CUS_CV_MDL = models.IntegerField()
    CUS_NAM_MDL = models.CharField(max_length = 60)
    CUS_TYP_MDL = models.CharField(max_length = 50)
    BUS_NAM_MDL = models.CharField(max_length = 50)
    SAL_NAM_MDL = models.CharField(max_length = 50)

class SalesPersonModel(models.Model):
    SAL_NAM_MDL = models.CharField(max_length = 50)
    SAL_ID_MDL = models.CharField(max_length = 10)
    SAL_BAS_MDL = models.CharField(max_length = 25,choices = Lotus_Salary_Base_Choices)
    class Meta:
        verbose_name =  'SALESPERSON'
        verbose_name_plural = 'SALESPERSON(s)'

class CustomerTypeModel(models.Model):
    CUS_TYPE_MDL = models.CharField(max_length = 25)
    class Meta:
        verbose_name = 'CUSTOMER TYPE'
        verbose_name_plural = "CUSTOMER TYPES"