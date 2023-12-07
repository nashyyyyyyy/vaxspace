from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vaxapp'

urlpatterns = [
    path('', views.login, name='login'),
    path('user_register/', views.user_register, name='user_register'),
    path('index/', views.index, name='index'),
    path('index/utilities/', views.utilities, name='utilities'),
    path('index/healthworker/', views.healthworker, name='healthworker'),
    path('index/barangay/', views.barangay, name='barangay'),
    path('index/guardian/', views.guardian, name='guardian'),
    path('add_healthworker/', views.add_healthworker, name='add_healthworker'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('admin_tables/', views.admin_tables, name='admin_tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('admin_tables/add_record/<int:id>/', views.add_record, name='admin_add_record'),
    path('tables/add_record/<int:id>/', views.add_record, name='add_record'), 
    path('tables/confirmation/<int:id>/', views.confirmation, name='confirmation'),
    path('logout/', views.logout, name='logout'),
]