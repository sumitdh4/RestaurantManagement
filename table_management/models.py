from django.db import models


class Table(models.Model):
    table_number = models.IntegerField()
    table_capacity = models.CharField(max_length=50)

    def __str__(self):
        return f" Table NO : {self.table_number} >> capacity : {self.table_capacity}"


