from django.contrib import admin

from measurement.models import Measurement, Sensor

# Register your models here.


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1
    readonly_fields = ['created_at',]


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    inlines = [MeasurementInline,]

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created_at',]
    readonly_fields = ['created_at',]

