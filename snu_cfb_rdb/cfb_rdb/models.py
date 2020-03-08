
# -*- coding: utf-8 -*-

import uuid

from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

# pathway.tsv
class PathwayType(models.Model):
    """done"""
    uid = models.CharField(primary_key=True, max_length=32, editable=False)
    name = models.CharField(null=False, unique=True, max_length=128)

    # class Meta:
    #     # todo set meta data...
    #     # manager = False
    #     db_table = 'pathway'

    def __str__(self):
        return self.name


# pathway_sub.tsv
class PathwaySub(models.Model):
    """done"""
    uid = models.CharField(primary_key=True, max_length=32, editable=False)
    name = models.CharField(null=False, unique=True, max_length=128)
    pathway_type = models.ForeignKey(
        PathwayType,
        to_field='uid',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


# disease.tsv
class Disease(models.Model):
    """done"""
    # id = models.AutoField(primary_key=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.CharField(null=False, unique=True, max_length=32)
    name = models.CharField(null=False, unique=True, max_length=128)

    def __str__(self):
        return self.name


# gene.tsv
class Gene(models.Model):
    """done"""
    """Duplicate entry error at name"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.CharField(null=False, max_length=32)
    name = models.CharField(null=False, max_length=64)

    def __str__(self):
        return self.name


# kegg.tsv
class Kegg(models.Model):
    """done"""
    """Searching error"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uid = models.CharField(max_length=32, editable=False)
    name = models.CharField(null=False, unique=True, max_length=128)
    pathway_type = models.ForeignKey(
        PathwayType,
        to_field='uid',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    pathway_sub = models.ForeignKey(
        PathwaySub,
        to_field='uid',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


# kegg_master.tsv
class KeggMaster(models.Model):
    # todo modify related_pathway, gene
    """
    django.db.utils.DataError: (1406, "Data too long for column 'gene_list' at row 1")
    """
    # https://cmleo.tistory.com/22
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kegg_name = models.ForeignKey(
        Kegg,
        to_field='id',
        null=False,
        on_delete=models.PROTECT
    )
    related_pathway = ListCharField(
        base_field=models.CharField(max_length=64),
        blank=True,
        null=True,
        max_length=128
    )
    disease_list = ListCharField(
        base_field=models.CharField(max_length=64),
        blank=True,
        null=True,
        max_length=128
    )
    gene_list = ListCharField(
        base_field=models.CharField(max_length=64),
        blank=True,
        null=True,
        max_length=128
    )
