"""
cfb_rdb.admin.py
"""
# -*- coding: utf-8 -*-

import csv

from django.contrib import admin
from .models import *
from django.http import HttpResponse


# Register your models here.

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = 'Export Selected'


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


class DiseaseAdmin(admin.ModelAdmin, ExportCsvMixin):
    """done"""
    list_display = ['id', 'uid', 'name']
    list_display_links = ['id', 'uid', 'name']
    search_fields = ['id', 'uid', 'name']
    actions = ['export_as_csv']


class GeneAdmin(admin.ModelAdmin):
    """done"""
    list_display = ['id', 'uid', 'name']
    list_display_links = ['id', 'uid', 'name']
    search_fields = ['id', 'uid', 'name']


class KeggAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'name', 'pathway_sub', 'pathway_type']
    list_display_links = ['id', 'uid', 'name', 'pathway_sub', 'pathway_type']
    search_fields = ['id', 'uid', 'name', 'pathway_sub', 'pathway_type']


class KeggMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'kegg_name', 'related_pathway', 'disease_list', 'gene_list']
    list_display_links = ['id', 'kegg_name', 'related_pathway', 'disease_list', 'gene_list']
    search_fields = ['id', 'kegg_name', 'related_pathway', 'disease_list', 'gene_list']


admin.site.register(PathwayType, PathwayTypeAdmin)
admin.site.register(PathwaySub, PathwaySubAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Gene, GeneAdmin)
admin.site.register(Kegg, KeggAdmin)
admin.site.register(KeggMaster, KeggMasterAdmin)
