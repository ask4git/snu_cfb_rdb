from django.contrib import admin
from .models import *


# Register your models here.


class PathwayTypeAdmin(admin.ModelAdmin):
    """done"""
    list_display = ['uid', 'name']
    list_display_links = ['uid', 'name']
    search_fields = ['uid', 'name']


class PathwaySubAdmin(admin.ModelAdmin):
    """done"""
    list_display = ['pathway_type', 'uid', 'name']
    list_display_links = ['pathway_type', 'uid', 'name']
    search_fields = ['pathway_type', 'uid', 'name']


class DiseaseAdmin(admin.ModelAdmin):
    """done"""
    list_display = ['id', 'uid', 'name']
    list_display_links = ['id', 'uid', 'name']
    search_fields = ['id', 'uid', 'name']


class GeneAdmin(admin.ModelAdmin):
    """done"""
    list_display = ['id', 'uid', 'name']
    list_display_links = ['id', 'uid', 'name']
    search_fields = ['id', 'uid', 'name']


class KeggAdmin(admin.ModelAdmin):
    list_display = ['pathway_type', 'pathway_sub', 'uid', 'name']
    list_display_links = ['pathway_type', 'pathway_sub', 'uid', 'name']
    search_fields = ['pathway_type', 'pathway_sub', 'uid', 'name']


# class KeggMasterAdmin(admin.ModelAdmin):
#     list_display = ['kegg_id', 'related_pathway', 'disease_list', 'gene_list']
#     list_display_links = ['kegg_id', 'related_pathway', 'disease_list', 'gene_list']
#     search_fields = ['kegg_id', 'related_pathway', 'disease_list', 'gene_list']


admin.site.register(PathwayType, PathwayTypeAdmin)
admin.site.register(PathwaySub, PathwaySubAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Gene, GeneAdmin)
admin.site.register(Kegg, KeggAdmin)
# admin.site.register(KeggMaster, KeggMasterAdmin)
