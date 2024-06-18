from django.contrib import admin
from .models import Chairs, Speciality,Testominal,Links,Team
from import_export.admin import ImportExportModelAdmin



@admin.register(Chairs)
class ChairAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'definition', 'slug', 'price','prices')
    prepopulated_fields = {'slug':('name', )}
    list_display_links = ('id', 'name', 'definition', 'price','prices')
    search_fields = ('name', 'id')
    ordering = ('id',)
    def definition(self, request):
        return request.definition[:5]
@admin.register(Speciality)
class SpecialityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'speciality','slug')
    prepopulated_fields = {'slug':('speciality', )}
    list_display_links = ('id', 'speciality')
    search_fields = ('speciality', 'id')
    ordering = ('id',)
    

@admin.register(Testominal)
class TestominalAdmin(ImportExportModelAdmin):
    list_display = ('id','slug', 'full_name','msg')
    prepopulated_fields = {'slug':('full_name', )}
    list_display_links = ('id', 'full_name','msg')
    search_fields = ( 'id','full_name')
    ordering = ('id',)
    def msg(self, request):
        return request.msg[:5]
    
    
admin.site.register(Links,ImportExportModelAdmin)


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'description','slug', 'full_name')
    prepopulated_fields = {'slug':('full_name', )}
    list_display_links = ('id', 'description','full_name')
    search_fields = ( 'id','full_name')
    ordering = ('id',)
    def description(self, request):
        return request.description[:5]

