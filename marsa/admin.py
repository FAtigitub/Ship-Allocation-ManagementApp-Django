from django.contrib import admin
from .models import *
# Register your models here.
class AdminPort(admin.ModelAdmin):
    list_display = ('name','location','last_update','save_by')

class AdminQuai(admin.ModelAdmin):
    list_display = ('nom','capacite','last_update','save_by','port')

class AdminPosteNavire(admin.ModelAdmin):
    list_display = ('nom','taille_max','quai_assigne','date_arrivee'
                    ,'heure_arrivee','date_depart','heure_depart','charge','description'
                    ,'save_by','last_update')
    
class AdminNavire(admin.ModelAdmin):
    list_display = ('numeroDeScanne','nom','type_marchandise','capacite','date_arrivee'
                    ,'heure_arrivee','date_depart','heure_depart','quai_de_preference','posteNavire'
                    ,'port','shifts_requis','save_by','last_update')

admin.site.register(Port, AdminPort)
admin.site.register(Quai, AdminQuai)
admin.site.register(PosteNavire, AdminPosteNavire)
admin.site.register(Navire, AdminNavire)    