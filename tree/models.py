from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import datetime


class Employee(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=100, db_index=True)
    position = models.CharField(max_length=100, db_index=True)
    emp_date = models.DateField()
    salary = models.DecimalField(max_digits=7, decimal_places=0)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        db_index=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
        self.emp_date = datetime.datetime.now()

