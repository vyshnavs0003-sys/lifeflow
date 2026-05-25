from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('user-dashboard/',views.user_dashboard,name='user_dashboard'),
    path('hospital-dashboard/',views.hospital_dashboard,name='hospital_dashboard'),
    path('add-inventory/',views.add_inventory,name='add_inventory',)
]