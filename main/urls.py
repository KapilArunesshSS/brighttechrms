from django.urls import path
from . import views

urlpatterns = [
        
    # Employee url Management
    path('', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    # authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),

    # url for the export feature 
    path('export/excel/', views.export_to_excel, name='export_excel'),

    #summary url
    path('api/summary/', views.monthly_summary_api, name='monthly_summary_api')
]


