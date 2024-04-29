from typing import Any
from django.db import models
from .models import CategoryLabel


class FieldMixin:
    is_custom = True
    category = None

    def __init__(self, *args: Any, category: CategoryLabel = None, **kwargs: Any) -> None:
        self.category = category
        return super().__init__(*args, **kwargs)


class AutoField(FieldMixin, models.AutoField):
    pass 

class BigAutoField(FieldMixin, models.BigAutoField):
    pass 

class BigIntegerField(FieldMixin, models.BigIntegerField):
    pass 

class BinaryField(FieldMixin, models.BinaryField):
    pass 

class BooleanField(FieldMixin, models.BooleanField):
    pass 

class CharField(FieldMixin, models.CharField):
    pass 

class CommaSeparatedIntegerField(FieldMixin, models.CommaSeparatedIntegerField):
    pass 

class DateField(FieldMixin, models.DateField):
    pass 

class DateTimeField(FieldMixin, models.DateTimeField):
    pass 

class DecimalField(FieldMixin, models.DecimalField):
    pass 

class DurationField(FieldMixin, models.DurationField):
    pass 

class EmailField(FieldMixin, models.EmailField):
    pass 

class Field(FieldMixin, models.Field):
    pass 

class FilePathField(FieldMixin, models.FilePathField):
    pass 

class FloatField(FieldMixin, models.FloatField):
    pass 

class GenericIPAddressField(FieldMixin, models.GenericIPAddressField):
    pass 

class IPAddressField(FieldMixin, models.IPAddressField):
    pass 

class IntegerField(FieldMixin, models.IntegerField):
    pass 

class NullBooleanField(FieldMixin, models.NullBooleanField):
    pass 

class PositiveBigIntegerField(FieldMixin, models.PositiveBigIntegerField):
    pass 

class PositiveIntegerField(FieldMixin, models.PositiveIntegerField):
    pass 

class PositiveSmallIntegerField(FieldMixin, models.PositiveSmallIntegerField):
    pass 

class SlugField(FieldMixin, models.SlugField):
    pass 

class SmallAutoField(FieldMixin, models.SmallAutoField):
    pass 

class SmallIntegerField(FieldMixin, models.SmallIntegerField):
    pass 

class TextField(FieldMixin, models.TextField):
    pass 

class TimeField(FieldMixin, models.TimeField):
    pass 

class URLField(FieldMixin, models.URLField):
    pass 

class UUIDField(FieldMixin, models.UUIDField):
    pass 

class FileField(FieldMixin, models.FileField):
    pass 

class ImageField(FieldMixin, models.ImageField):
    pass 

class JSONField(FieldMixin, models.JSONField):
    pass 

class OneToOneField(FieldMixin, models.OneToOneField):
    pass 

class ManyToManyField(FieldMixin, models.ManyToManyField):
    pass 

class ForeignKey(FieldMixin, models.ForeignKey):
    pass 