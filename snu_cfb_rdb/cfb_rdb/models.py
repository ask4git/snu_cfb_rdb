
# -*- coding: utf-8 -*-

from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

# pathway.tsv
class PathwayType(models.Model):
    """done"""
    pathway_type_id = models.CharField(primary_key=True, max_length=32)
    pathway_type_name = models.CharField(blank=False, unique=True, max_length=128)

    # class Meta:
    #     # todo set meta data...
    #     # manager = False
    #     db_table = 'pathway'

    def __str__(self):
        return self.pathway_type_name


# pathway_sub.tsv
class PathwaySub(models.Model):
    """done"""
    pathway_sub_id = models.CharField(primary_key=True, max_length=32)
    pathway_sub_name = models.CharField(blank=False, unique=True, max_length=128)
    pathway_type_name = models.ForeignKey(
        PathwayType,
        to_field='pathway_type_id',
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.pathway_sub_name


# disease.tsv
class Disease(models.Model):
    """done"""
    disease_id = models.CharField(primary_key=True, max_length=32)
    disease_name = models.CharField(blank=False, unique=True, max_length=128)

    def __str__(self):
        return self.disease_name


# gene.tsv
class Gene(models.Model):
    gene_id = models.CharField(primary_key=True, max_length=32)
    gene_name = models.CharField(blank=False, null=False, max_length=64)

    def __str__(self):
        return self.gene_name


# kegg.tsv
class Kegg(models.Model):
    kegg_id = models.CharField(primary_key=True, max_length=32)
    kegg_name = models.CharField(blank=False, null=False, max_length=128)

    def __str__(self):
        return self.kegg_name


# kegg_master.tsv
class KeggMaster(models.Model):
    # todo modify related_pathway, gene
    kegg_id = pathway_type_name = models.ForeignKey(
        Kegg,
        to_field='kegg_id',
        blank=True,
        on_delete=models.CASCADE
    )
    related_pathway = ListCharField(base_field=models.CharField())
    disease_list = ListCharField(base_field=models.CharField())
    gene_list = ListCharField(base_field=models.CharField())
