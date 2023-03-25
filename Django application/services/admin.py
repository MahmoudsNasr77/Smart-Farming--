from django.contrib import admin
from .models import croppredictions,waterpredictions
from import_export.admin import ImportExportModelAdmin


@admin.register(croppredictions)
class CropPredictionsAdmin(ImportExportModelAdmin):
    pass
@admin.register(waterpredictions)
class WaterPredictionsAdmin(ImportExportModelAdmin):
    pass