from django.db import models
from table_management.models import Table
from menu_management.models import Items


class Orders(models.Model):
    order_number = models.IntegerField()
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)
    discount = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f" Order no. {str(self.order_number)}  ---- for {str(self.table_number)} ----  is {'Active' if self.active else 'Completed'}"
