from django.db import models
from django.contrib.auth.models import User
class croppredictions(models.Model):
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    N = models.DecimalField(max_digits=15, decimal_places=7)
    P = models.DecimalField(max_digits=15, decimal_places=7)
    K = models.DecimalField(max_digits=15, decimal_places=7)
    temperature = models.DecimalField(max_digits=15, decimal_places=7)
    humidity = models.DecimalField(max_digits=15, decimal_places=7)
    ph = models.DecimalField(max_digits=15, decimal_places=7)
    rainfall = models.DecimalField(max_digits=15, decimal_places=7)
    perviouspredictions = models.CharField(max_length=500)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="UserCropPredictions", null=True)

    def __str__(self):
        return self.perviouspredictions

    class Meta:
        verbose_name_plural = "CropPredictions"

class waterpredictions(models.Model):
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    temperature = models.DecimalField(max_digits=15, decimal_places=7)
    humidity = models.DecimalField(max_digits=15, decimal_places=7)
    soilMoisture=models.DecimalField(max_digits=15, decimal_places=7)
    waterLevel=models.DecimalField(max_digits=15, decimal_places=7)
    lighting = models.DecimalField(max_digits=15, decimal_places=7)
    crop_type = models.CharField(max_length=100, choices=[('Pepper', 'Pepper'), ('Strawberry', 'Strawberry'), ('Tomatoes', 'Tomatoes')])
    water_loss=models.DecimalField(max_digits=15, decimal_places=7)
    actual = models.DecimalField(max_digits=15, decimal_places=7)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="UserwaterPredictions", null=True)
    class Meta:
        verbose_name_plural = "WaterPredictions"

