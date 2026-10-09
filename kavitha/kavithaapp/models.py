from django.db import models
from django.contrib import admin
class Blinket(models.Model):
    CustomerName=models.CharField(max_length=10)
    Products=models.CharField(max_length=10)
    Mobile=models.IntegerField(primary_key=True)
    Orders=models.CharField(max_length=10)
    Payment=models.FloatField()
    Details=models.TextField()
class BlinketAdmin(admin.ModelAdmin):
    list_display=["CustomerName","Products","Mobile","Orders","Payment","Details",]