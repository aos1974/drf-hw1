from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, null=False, verbose_name='sensor')
    description = models.CharField(max_length=50, blank=True, verbose_name='description')

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, blank=False, null=False)
    temperature = models.DecimalField(max_digits=4, decimal_places=2, default=-333, blank=False, verbose_name='temperature')
    created_at = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='date')

    class Meta:
        verbose_name = 'Показание датчика'
        verbose_name_plural = 'Показания датчиков'
        ordering = ['-created_at',]