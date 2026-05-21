from django.contrib import admin
from .models import Donor, Hospital, BloodInventrory, BloodRequest
# Register your models here.

admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(BloodInventrory)
admin.site.register(BloodRequest)