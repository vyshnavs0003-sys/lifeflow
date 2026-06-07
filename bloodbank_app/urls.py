from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('user-dashboard/',views.user_dashboard,name='user_dashboard'),
    path('hospital-dashboard/',views.hospital_dashboard,name='hospital_dashboard'),
    path('add-inventory/',views.add_inventory,name='add_inventory'),
    path('update-inventry/<int:inventory_id>/',views.update_inventory,name='update_inventory'),
    path('delete-inventory/<int:inventory_id>/',views.delete_inventory,name='delete_inventory'),
    path('check-availability/',views.check_availability,name='check_availability'),
    path('become-donor/',views.become_donor,name='become_donor'),
    path('donor-profile/',views.donor_profile,name='donor_profile'),
    path('donor-profile/edit/',views.edit_donor_profile,name='edit_donor_profile'),
    path('donor-list/',views.donor_list,name='donor_list'),
    path('request-blood/',views.request_blood,name='request_blood'),
    path('my-blood-requests/',views.my_blood_requests,name='my_blood_requests'),
    path('hospita;-blood-requests/',views.hospital_blood_requests,name='hospital_blood_requests'),
    path('update-request-status/<int:request_id>/<str:status>/',views.update_request_status,name='update_request_status'),
]