from django.contrib import admin
from .models import Donor, Hospital, BloodInventory, BloodRequest
# Register your models here.

class DonorAdmin(admin.ModelAdmin):
    list_display = ['donor_name','blood_group','phone','location','age','last_donation_date']
    search_fields = ['donor|_name','blood_group','location']
    list_filter = [ 'blood_group','location']
    ordering = ['id']
    list_per_page = 10


class HospitalAdmin(admin.ModelAdmin):
    list_display = ['hospital_name','location','contact']
    search_fields = ['hospital_name','location']
    list_filter = ['location']



class BloodInventoryAdmin(admin.ModelAdmin):
    list_display = ['hospital', 'blood_group','units_available']
    search_fields = ['hospital','blood_group']
    list_filter = ['blood_group']
    



class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ['patient_name','blood_group_needed','units_needed','hospital','status','required_date']
    search_fields = ['patient_name','blood_group_needed','patient_id']
    list_filter = ['blood_group_needed','status','hospital']

admin.site.register(Donor,DonorAdmin)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(BloodInventory,BloodInventoryAdmin)
admin.site.register(BloodRequest,BloodRequestAdmin)