from django.contrib import admin
from .models import *

# Register your models here.


class PathwayTypeAdmin(admin.ModelAdmin):
    list_display = ['pathway_type_id', 'pathway_type_name']
    list_display_links = ['pathway_type_id', 'pathway_type_name']
    search_fields = ['pathway_type_id', 'pathway_type_name']


class PathwaySubAdmin(admin.ModelAdmin):
    list_display = ['pathway_type_name', 'pathway_sub_name', 'pathway_sub_id']
    list_display_links = ['pathway_type_name', 'pathway_sub_name', 'pathway_sub_id']
    search_fields = ['pathway_type_name', 'pathway_sub_name', 'pathway_sub_id']


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['disease_id', 'disease_name']
    list_display_links = ['disease_id', 'disease_name']
    search_fields = ['disease_id', 'disease_name']


class GeneAdmin(admin.ModelAdmin):
    list_display = ['gene_id', 'gene_name']
    list_display_links = ['gene_id', 'gene_name']
    search_fields = ['gene_id', 'gene_name']


class KeggAdmin(admin.ModelAdmin):
    list_display = ['kegg_id', 'kegg_name']
    list_display_links = ['kegg_id', 'kegg_name']
    search_fields = ['kegg_id', 'kegg_name']


admin.site.register(PathwayType, PathwayTypeAdmin)
admin.site.register(PathwaySub, PathwaySubAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Gene, GeneAdmin)
admin.site.register(Kegg, KeggAdmin)
