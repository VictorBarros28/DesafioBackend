from django.contrib import admin
from django.http import response
from . import models
from django.shortcuts import render
from .models import Planilha
import csv
from info.models import Processo
# Register your models here.

def Cadastrar_Processos(modeladmin,request,queryset):
    for q in queryset:

            obj = Planilha.objects.get()
            with open(obj.arquivo.path, 'r') as x:
                
                reader = csv.reader(x)
            
                for i, row in enumerate(reader):
                        if i==0:
                            pass
                       
                        else:
                            str = row[0].split(';')
                            print(row)
                            Processo.objects.create(
                            pasta = str[0], comarca = str[1], uf= str[2]                        
                        )   
            obj.save()    
    
class PlanilhaAdmin(admin.ModelAdmin):
    list_display = ['nome','cliente']
    actions = [Cadastrar_Processos]
   
admin.site.register(Planilha, PlanilhaAdmin)