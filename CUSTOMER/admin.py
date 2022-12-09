from django.contrib import admin
from .models import SalesPersonModel

# Register your models here.

class SalesPersonAdmin(admin.ModelAdmin):
    list_display =['SAL_NAM_MDL','SAL_ID_MDL','SAL_BAS_MDL']
    list_filter = ['SAL_BAS_MDL']
admin.site.register(SalesPersonModel,SalesPersonAdmin)